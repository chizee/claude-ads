"""Shared URL validation utilities with SSRF protection.

Used by fetch_page.py, analyze_landing.py, capture_screenshot.py, and
generate_image.py to validate user-supplied URLs before making HTTP requests
or launching browsers, and to sanitize exception messages before surfacing
them to the user.
"""

import ipaddress
import os
import re
import socket
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

try:
    import requests
    from requests.adapters import HTTPAdapter
    from requests.exceptions import InvalidURL
except ImportError:  # pragma: no cover - callers surface their dependency error
    requests = None
    HTTPAdapter = object  # type: ignore[assignment,misc]

    class InvalidURL(ValueError):
        """Fallback used only when Requests is not installed."""

# Sensitive substrings to redact from any error message before logging or
# returning to the caller. Catches common credential parameter names (api_key,
# apikey, access_token, refresh_token, auth, key, token, secret, password,
# OAuth `code=`, AWS `signature=`) and bare `Bearer <token>` headers
# regardless of case.
_SENSITIVE_PATTERN = re.compile(
    r'\b(api[_-]?key|access[_-]?token|refresh[_-]?token|authorization|auth|key|token|secret|password|code|signature)'
    r'\s*[=:]\s*[\"\']?(?:Bearer\s+)?[^\s&,;\"\']+|\bBearer\s+[^\s,;]+',
    re.IGNORECASE,
)

_TOKEN_PATTERN = re.compile(
    r"\b(?:sk[_-](?:live[_-])?|gh[pousr]_|AIza)[A-Za-z0-9._-]{8,}\b",
    re.IGNORECASE,
)

_PRIVATE_KEY_PATTERN = re.compile(
    r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?-----END [A-Z0-9 ]*PRIVATE KEY-----",
    re.DOTALL,
)

_SENSITIVE_HEADERS = {
    "authorization",
    "cookie",
    "proxy-authorization",
    "set-cookie",
    "x-api-key",
    "x-auth-token",
}


def _redact_sensitive(text: str) -> str:
    """Run the credential-redaction regex over arbitrary text."""
    text = _PRIVATE_KEY_PATTERN.sub("[REDACTED PRIVATE KEY]", text)
    text = _SENSITIVE_PATTERN.sub(
        lambda m: (
            "authorization=Bearer ***"
            if m.group(1) and m.group(1).lower() == "authorization" and "bearer" in m.group(0).lower()
            else (m.group(1).lower().replace('-', '_') + '=***')
            if m.group(1)
            else 'Bearer ***'
        ),
        text,
    )
    return _TOKEN_PATTERN.sub("***", text)


def redact_sensitive_text(value: Any) -> str:
    """Return a log-safe string with common credentials removed."""
    return _redact_sensitive(str(value))


def sanitize_error(err: Exception) -> str:
    """Strip potential API keys / tokens / passwords from an exception message.

    Use whenever an exception's str() reaches stdout, JSON output, or a user-
    facing error field. The redaction is irreversible — the goal is to make
    the message safe to log, not to preserve the original details.

    Args:
        err: The exception to format.

    Returns:
        The exception string with sensitive substrings replaced.
    """
    return redact_sensitive_text(err)


def sanitize_headers(headers: Any) -> dict[str, str]:
    """Return response/request headers with credential-bearing values removed."""
    sanitized: dict[str, str] = {}
    for name, value in dict(headers or {}).items():
        key = str(name)
        if key.lower() in _SENSITIVE_HEADERS:
            sanitized[key] = "***"
        else:
            sanitized[key] = redact_sensitive_text(value)
    return sanitized


def sanitize_url(url: str) -> str:
    """Strip credentials from a URL string before logging it to stderr or stdout.

    Covers tokens embedded in query parameters (`?access_token=...&code=...`)
    and userinfo (`https://user:password@host/`). The output is meant to be
    safe to surface in CLI output, logs, or transcripts — not round-trippable.

    Args:
        url: The URL to sanitize.

    Returns:
        URL with credential-bearing values replaced by `***`.
    """
    # Drop userinfo segment if present (https://user:pass@host -> https://host)
    parsed = urlparse(url)
    if parsed.username or parsed.password:
        netloc = parsed.hostname or ''
        try:
            if parsed.port:
                netloc = f"{netloc}:{parsed.port}"
        except ValueError:
            # The URL will be rejected by validate_url; redaction must still
            # be fail-safe and never expose userinfo while formatting errors.
            pass
        url = parsed._replace(netloc=netloc).geturl()
    # Redact sensitive query/fragment parameters and token-looking values.
    return _redact_sensitive(url)

_MAX_URL_LENGTH = 8192
_LOCAL_HOSTNAMES = {"localhost", "localhost.localdomain", "metadata", "metadata.google.internal"}


def _validate_and_resolve_url(url: str) -> tuple[str, Any, tuple[str, ...]]:
    """Validate a URL and return every public address from one DNS snapshot.

    The returned addresses are suitable for connection pinning. Callers must
    not validate the hostname here and then resolve it again while connecting:
    doing so would recreate the DNS rebinding/TOCTOU window this helper exists
    to close.
    """
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    url = url.strip()
    if not url or len(url) > _MAX_URL_LENGTH:
        raise ValueError("URL is empty or too long.")
    if any(ord(char) < 32 for char in url) or "\\" in url:
        raise ValueError("URL contains forbidden control characters or backslashes.")

    parsed = urlparse(url)
    if not parsed.scheme:
        url = f"https://{url}"
        parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Invalid URL scheme: {parsed.scheme}. Only http/https allowed.")
    hostname = parsed.hostname
    if not hostname:
        raise ValueError("URL has no hostname.")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Credentials in URLs are not allowed.")
    try:
        parsed.port
    except ValueError as exc:
        raise ValueError("URL has an invalid port.") from exc

    normalized_hostname = hostname.rstrip(".").lower()
    if normalized_hostname in _LOCAL_HOSTNAMES or normalized_hostname.endswith(".localhost"):
        raise ValueError("URL targets a local/internal hostname.")
    try:
        resolved = socket.getaddrinfo(
            normalized_hostname,
            None,
            socket.AF_UNSPEC,
            socket.SOCK_STREAM,
        )
    except socket.gaierror as exc:
        raise ValueError(f"DNS resolution failed for {normalized_hostname}: {exc}") from exc
    if not resolved:
        raise ValueError(f"DNS resolution returned no addresses for {normalized_hostname}")

    addresses: list[str] = []
    for _, _, _, _, addr in resolved:
        ip = ipaddress.ip_address(addr[0])
        # is_global rejects loopback, private, link-local, multicast,
        # documentation, benchmark, CGNAT, unspecified, and reserved space.
        if not ip.is_global or ip.is_multicast or ip.is_reserved:
            raise ValueError(f"URL resolves to blocked non-public IP: {ip}")
        canonical = str(ip)
        if canonical not in addresses:
            addresses.append(canonical)
    return url, parsed, tuple(addresses)


def validate_url(url: str) -> str:
    """Validate URL scheme and block private/internal IPs (SSRF protection).

    Args:
        url: The URL to validate. If no scheme, https:// is prepended.

    Returns:
        The validated URL string (with scheme).

    Raises:
        ValueError: If URL has invalid scheme, no hostname, resolves to
                    a blocked IP, or DNS resolution fails.
    """
    validated, _, _ = _validate_and_resolve_url(url)
    return validated


def validate_browser_url(url: str, *, egress_sandbox_attested: bool = False) -> str:
    """Validate a URL at the strongest boundary Playwright can enforce.

    Playwright route interception sees a URL before Chromium performs its own
    DNS lookup, but it cannot pin the later socket to the address Python
    validated. Browser dispatch is therefore denied by default, including for
    public IP literals. Callers may proceed only after explicitly attesting
    that an independently configured OS/container egress boundary blocks
    private, loopback, link-local, metadata, and other non-public destinations
    after DNS resolution and across redirects. The attestation is a contract;
    this module cannot inspect or establish that external sandbox.
    """
    validated, _, _ = _validate_and_resolve_url(url)
    if not egress_sandbox_attested:
        raise ValueError(
            "Browser request blocked: Playwright cannot pin DNS at the socket "
            "boundary. An explicit OS/container egress-sandbox attestation is "
            "required; use the Requests-based fetcher otherwise."
        )
    return validated


def _origin_prefix(parsed: Any) -> str:
    """Return the exact Requests adapter mount prefix for a parsed origin."""
    # Preserve an explicitly written default port and a trailing DNS dot. A
    # normalized prefix such as ``https://example.com/`` does not match
    # Requests' URL ``https://example.com:443/`` and would silently fall
    # through to the ordinary, unpinned HTTPS adapter.
    return f"{parsed.scheme}://{parsed.netloc.lower()}/"


class _PinnedHTTPAdapter(HTTPAdapter):
    """Requests adapter that connects to a validated IP without re-resolving.

    The request URL and HTTP Host header remain hostname-based. For HTTPS,
    ``server_hostname`` preserves SNI and ``assert_hostname`` preserves normal
    certificate hostname verification while the pool's socket target is the
    pinned numeric address.
    """

    def __init__(self, parsed: Any, addresses: tuple[str, ...]) -> None:
        if HTTPAdapter is object:  # pragma: no cover - dependency guard
            raise RuntimeError("requests is required for guarded HTTP requests")
        super().__init__()
        self._scheme = parsed.scheme
        self._hostname = parsed.hostname.rstrip(".").lower()
        self._port = parsed.port
        self._address = addresses[0]

    def _check_request_origin(self, request: Any) -> Any:
        parsed = urlparse(request.url)
        hostname = (parsed.hostname or "").rstrip(".").lower()
        if (
            parsed.scheme != self._scheme
            or hostname != self._hostname
            or parsed.port != self._port
        ):
            raise InvalidURL("Pinned adapter cannot be reused for another origin.")
        return parsed

    def get_connection_with_tls_context(
        self,
        request: Any,
        verify: Any,
        proxies: Any = None,
        cert: Any = None,
    ) -> Any:
        parsed = self._check_request_origin(request)
        if proxies:
            raise InvalidURL("Proxies are forbidden for guarded requests.")
        if parsed.scheme == "https" and verify is False:
            raise InvalidURL("TLS certificate verification cannot be disabled.")

        host_params, pool_kwargs = self.build_connection_pool_key_attributes(
            request,
            verify,
            cert,
        )
        host_params["host"] = self._address
        if parsed.scheme == "https":
            pool_kwargs["server_hostname"] = self._hostname
            pool_kwargs["assert_hostname"] = self._hostname

        # PreparedRequest does not add Host itself; urllib3 would otherwise
        # derive it from the pinned IP pool and break virtual hosting.
        default_port = 443 if parsed.scheme == "https" else 80
        bracketed = f"[{self._hostname}]" if ":" in self._hostname else self._hostname
        request.headers["Host"] = (
            bracketed
            if parsed.port in (None, default_port)
            else f"{bracketed}:{parsed.port}"
        )
        return self.poolmanager.connection_from_host(
            **host_params,
            pool_kwargs=pool_kwargs,
        )


def guarded_request(session: Any, method: str, url: str, **kwargs: Any) -> Any:
    """Validate and address-pin an outbound Requests dispatch.

    Automatic redirects are disabled because every redirect target must return
    to this boundary for a fresh validation. The adapter connects to an IP from
    the same DNS snapshot that passed policy, closing the validation/connect
    TOCTOU window without changing Host, SNI, or TLS hostname verification.
    """
    if requests is None:  # pragma: no cover - dependency guard
        raise ValueError("requests is required for guarded HTTP requests.")
    if not isinstance(url, str):
        raise ValueError("URL must be a string.")
    raw_url = url.strip()
    if any(ord(char) < 32 for char in raw_url) or "\\" in raw_url:
        raise ValueError("URL contains forbidden control characters or backslashes.")
    if not urlparse(raw_url).scheme:
        raw_url = f"https://{raw_url}"
    try:
        # Requests canonicalizes IDNs before adapter selection. Validate and
        # mount against that same form; mounting the caller's Unicode netloc
        # would let the prepared punycode URL fall through to the default
        # unpinned adapter.
        canonical_url = requests.Request(method.upper(), raw_url).prepare().url
    except (requests.exceptions.RequestException, ValueError) as exc:
        raise ValueError(f"Invalid URL: {sanitize_error(exc)}") from exc

    validated, parsed, addresses = _validate_and_resolve_url(canonical_url)
    if kwargs.get("allow_redirects") is True:
        raise ValueError("Automatic redirects are forbidden for guarded requests.")
    if parsed.scheme == "https" and kwargs.get("verify") is False:
        raise ValueError("TLS certificate verification cannot be disabled.")
    if kwargs.get("proxies"):
        raise ValueError("Proxies are forbidden for guarded requests.")
    kwargs["allow_redirects"] = False

    if not hasattr(session, "mount"):
        # Existing callers historically passed the requests module. Replace it
        # with an isolated Session rather than using the module-level pool,
        # which cannot be safely pinned.
        if requests is None or session is not requests:
            raise ValueError("guarded_request requires requests.Session.")
        session = requests.Session()
        session.trust_env = False

    adapter = _PinnedHTTPAdapter(parsed, addresses)
    session.mount(_origin_prefix(parsed), adapter)
    get_adapter = getattr(session, "get_adapter", None)
    if get_adapter is not None and get_adapter(validated) is not adapter:
        raise ValueError("Pinned adapter selection failed; request denied.")
    dispatcher = getattr(session, method.lower(), None)
    if dispatcher is None:
        raise ValueError(f"Unsupported HTTP method: {method}")
    return dispatcher(validated, **kwargs)


def install_playwright_ssrf_guard(
    context: Any,
    *,
    egress_sandbox_attested: bool = False,
) -> list[dict[str, str]]:
    """Screen every Playwright request before dispatch.

    Context-level routing covers the main frame, redirects, child frames, and
    subresources. Callers must create the context with service workers blocked,
    because service-worker initiated requests can bypass Playwright routing.
    The returned list records sanitized blocked requests for user-facing errors.
    """
    blocked: list[dict[str, str]] = []

    def guard(route: Any, request: Any = None) -> None:
        outbound = request or route.request
        try:
            validate_browser_url(
                outbound.url,
                egress_sandbox_attested=egress_sandbox_attested,
            )
        except (TypeError, ValueError) as exc:
            blocked.append({"url": sanitize_url(str(outbound.url)), "error": sanitize_error(exc)})
            route.abort("blockedbyclient")
            return
        route.continue_()

    context.route("**/*", guard)
    return blocked


def create_guarded_browser_context(browser: Any, **kwargs: Any) -> tuple[Any, list[dict[str, str]]]:
    """Create a guarded Playwright context.

    ``egress_sandbox_attested`` is consumed here rather than passed to
    Playwright. Its default is intentionally false, which makes every browser
    request fail closed at the route boundary.
    """
    egress_sandbox_attested = bool(kwargs.pop("egress_sandbox_attested", False))
    kwargs.setdefault("service_workers", "block")
    kwargs.setdefault("accept_downloads", False)
    context = browser.new_context(**kwargs)
    return context, install_playwright_ssrf_guard(
        context,
        egress_sandbox_attested=egress_sandbox_attested,
    )


def output_root(root: str | os.PathLike[str] | None = None) -> Path:
    """Resolve the only directory in which generated artifacts may be written."""
    configured = root or os.environ.get("CLAUDE_ADS_OUTPUT_ROOT") or os.getcwd()
    return Path(configured).expanduser().resolve()


def resolve_output_path(
    path: str | os.PathLike[str],
    *,
    root: str | os.PathLike[str] | None = None,
    create_parent: bool = False,
) -> Path:
    """Resolve an output path and reject traversal or symlink escapes.

    Relative paths are anchored to ``CLAUDE_ADS_OUTPUT_ROOT`` (or the current
    directory). Absolute paths are accepted only when they remain inside that
    root. Existing symlinks are resolved before the containment check.
    """
    base = output_root(root)
    candidate = Path(path).expanduser()
    if not candidate.is_absolute():
        candidate = base / candidate
    candidate = candidate.resolve(strict=False)
    try:
        candidate.relative_to(base)
    except ValueError as exc:
        raise ValueError(f"Output path escapes configured root: {candidate}") from exc
    if create_parent:
        candidate.parent.mkdir(parents=True, exist_ok=True)
    return candidate
