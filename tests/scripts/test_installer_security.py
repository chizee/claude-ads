"""Installer ownership and dependency-isolation regression tests."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
BASH_INSTALLER_ONLY = pytest.mark.skipif(
    os.name == "nt", reason="Bash installer behavior is exercised on Unix runners"
)


def _run(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    if os.name == "nt":
        pytest.skip("Bash installer behavior is exercised on Linux and macOS runners")
    return subprocess.run(
        ["bash", str(ROOT / script), *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def _fake_python(tmp_path: Path, target: str, fail_venv: bool = False) -> Path:
    directory = tmp_path / "fake-bin"
    directory.mkdir()
    script = directory / "python3"
    if target.count("|") == 3:
        target += "|glibc|2.17|supported" if "|linux|" in target else "|none|11.0|supported"
    script.write_text(
        "#!/bin/sh\n"
        f"if [ \"$1\" = \"-c\" ]; then printf '%s\\n' '{target}'; exit 0; fi\n"
        + ("exit 42\n" if fail_venv else "exec /usr/bin/python3 \"$@\"\n"),
        encoding="utf-8",
    )
    script.chmod(0o755)
    return directory


def _install(tmp_path: Path) -> tuple[Path, Path]:
    skills = tmp_path / "skills"
    agents = tmp_path / "agents"
    result = _run(
        "install.sh",
        "--target=claude",
        "--source=local",
        "--no-deps",
        f"--skill-dir={skills}",
        f"--agent-dir={agents}",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    return skills, agents


@BASH_INSTALLER_ONLY
def test_bash_installer_syntax_and_no_global_pip_escape_hatch():
    for script in ("install.sh", "uninstall.sh"):
        result = subprocess.run(
            ["bash", "-n", str(ROOT / script)], capture_output=True, text=True, check=False
        )
        assert result.returncode == 0, result.stderr

    installer = (ROOT / "install.sh").read_text(encoding="utf-8")
    assert "--break-system-packages" not in installer
    assert "curl -fsSL" not in installer
    assert "python3 -m venv" in installer
    assert "--require-hashes --only-binary=:all:" in installer
    assert "-m pip check" in installer
    assert "requirements.lock" in installer
    assert "--report" in installer
    assert "write_install_receipt.py" in installer
    assert "managed-runtime-receipt.json" in installer
    assert "banana-claude" not in installer

    powershell = (ROOT / "install.ps1").read_text(encoding="utf-8")
    assert "--require-hashes --only-binary=:all:" in powershell
    assert "-m pip check" in powershell
    assert "requirements.lock" in powershell
    assert "--report" in powershell
    assert "write_install_receipt.py" in powershell
    assert "managed-runtime-receipt.json" in powershell
    assert "banana-claude" not in powershell


@BASH_INSTALLER_ONLY
def test_manifest_owned_uninstall_preserves_unrelated_ads_skill(tmp_path):
    skills, agents = _install(tmp_path)
    assert (skills / "ads" / "requirements.lock").is_file()
    unrelated = skills / "ads-user-owned"
    unrelated.mkdir()
    (unrelated / "SKILL.md").write_text("user data", encoding="utf-8")

    result = _run(
        "uninstall.sh",
        "--target=claude",
        f"--skill-dir={skills}",
        f"--agent-dir={agents}",
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert not (skills / "ads" / "SKILL.md").exists()
    assert not (skills / "ads" / "requirements.lock").exists()
    assert unrelated.joinpath("SKILL.md").read_text(encoding="utf-8") == "user data"
    assert not (skills / ".claude-ads-claude.manifest").exists()


@BASH_INSTALLER_ONLY
def test_installer_includes_portable_interface_and_all_platform_surfaces(tmp_path):
    skills, agents = _install(tmp_path)
    assert (skills / "ads" / "agents" / "openai.yaml").is_file()
    for platform in (
        "google", "meta", "youtube", "linkedin", "tiktok", "microsoft",
        "apple", "amazon", "reddit", "pinterest", "snapchat", "x",
    ):
        assert (skills / f"ads-{platform}" / "SKILL.md").is_file()
        assert (agents / f"audit-{platform}.md").is_file()


@BASH_INSTALLER_ONLY
def test_tampered_manifest_fails_before_removing_files(tmp_path):
    skills, agents = _install(tmp_path)
    manifest = skills / ".claude-ads-claude.manifest"
    with manifest.open("a", encoding="utf-8") as handle:
        handle.write(f"F\t{tmp_path.parent / 'outside.txt'}\n")

    result = _run(
        "uninstall.sh",
        "--target=claude",
        f"--skill-dir={skills}",
        f"--agent-dir={agents}",
    )
    assert result.returncode != 0
    assert "Unsafe ownership-manifest path" in result.stderr
    assert (skills / "ads" / "SKILL.md").exists()


@BASH_INSTALLER_ONLY
def test_installer_refuses_symlink_escape(tmp_path):
    skills = tmp_path / "skills"
    agents = tmp_path / "agents"
    outside = tmp_path / "outside"
    skills.mkdir()
    outside.mkdir()
    (skills / "ads").symlink_to(outside, target_is_directory=True)

    result = _run(
        "install.sh",
        "--target=claude",
        "--source=local",
        "--no-deps",
        f"--skill-dir={skills}",
        f"--agent-dir={agents}",
    )
    assert result.returncode != 0
    assert "Refusing symlinked install directory" in result.stderr
    assert not (outside / "SKILL.md").exists()


@BASH_INSTALLER_ONLY
def test_unsupported_python_fails_before_any_destination_mutation(tmp_path):
    skills, agents = tmp_path / "skills", tmp_path / "agents"
    fake_bin = _fake_python(tmp_path, "cpython|3.14|linux|x86_64")
    result = subprocess.run(
        ["bash", str(ROOT / "install.sh"), "--target=claude", "--source=local", f"--skill-dir={skills}", f"--agent-dir={agents}"],
        cwd=ROOT, env={**os.environ, "PATH": f"{fake_bin}:{os.environ['PATH']}"}, capture_output=True, text=True, check=False,
    )
    assert result.returncode != 0
    assert "No verified dependency lock target" in result.stderr
    assert not skills.exists()
    assert not agents.exists()


@BASH_INSTALLER_ONLY
def test_musl_linux_fails_before_any_destination_mutation(tmp_path):
    skills, agents = tmp_path / "skills", tmp_path / "agents"
    fake_bin = _fake_python(tmp_path, "cpython|3.12|linux|x86_64|musl|1.2.5|unsupported")
    result = subprocess.run(
        ["bash", str(ROOT / "install.sh"), "--target=claude", "--source=local", f"--skill-dir={skills}", f"--agent-dir={agents}"],
        cwd=ROOT, env={**os.environ, "PATH": f"{fake_bin}:{os.environ['PATH']}"}, capture_output=True, text=True, check=False,
    )
    assert result.returncode != 0
    assert "musl Linux is unsupported" in result.stderr
    assert not skills.exists()
    assert not agents.exists()


@BASH_INSTALLER_ONLY
def test_dependency_failure_leaves_complete_ownership_manifest_for_uninstall(tmp_path):
    skills, agents = tmp_path / "skills", tmp_path / "agents"
    stale_receipt = skills / "ads" / "managed-runtime-receipt.json"
    stale_receipt.parent.mkdir(parents=True)
    stale_receipt.write_text('{"stale": true}\n', encoding="utf-8")
    fake_bin = _fake_python(tmp_path, "cpython|3.12|linux|x86_64", fail_venv=True)
    result = subprocess.run(
        ["bash", str(ROOT / "install.sh"), "--target=claude", "--source=local", f"--skill-dir={skills}", f"--agent-dir={agents}"],
        cwd=ROOT, env={**os.environ, "PATH": f"{fake_bin}:{os.environ['PATH']}"}, capture_output=True, text=True, check=False,
    )
    assert result.returncode != 0
    assert (skills / ".claude-ads-claude.manifest").is_file()
    assert (skills / "ads" / "requirements.lock").is_file()
    assert not stale_receipt.exists()
    uninstall = _run("uninstall.sh", "--target=claude", f"--skill-dir={skills}", f"--agent-dir={agents}")
    assert uninstall.returncode == 0, uninstall.stdout + uninstall.stderr
    assert not (skills / "ads" / "requirements.lock").exists()


@BASH_INSTALLER_ONLY
def test_manifest_traversal_is_rejected_before_removal(tmp_path):
    skills, agents = _install(tmp_path)
    manifest = skills / ".claude-ads-claude.manifest"
    with manifest.open("a", encoding="utf-8") as handle:
        handle.write(f"F\t{skills / 'ads' / '..' / '..' / 'outside.txt'}\n")

    result = _run(
        "uninstall.sh",
        "--target=claude",
        f"--skill-dir={skills}",
        f"--agent-dir={agents}",
    )
    assert result.returncode != 0
    assert (skills / "ads" / "SKILL.md").exists()


@pytest.mark.skipif(shutil.which("pwsh") is None, reason="PowerShell is not installed")
@pytest.mark.parametrize("script", ["install.ps1", "uninstall.ps1"])
def test_powershell_scripts_parse(script):
    command = f"[void][scriptblock]::Create((Get-Content -Raw '{ROOT / script}'))"
    result = subprocess.run(
        ["pwsh", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


@pytest.mark.skipif(shutil.which("pwsh") is None, reason="PowerShell is not installed")
def test_powershell_install_uninstall_round_trip_preserves_unrelated_skill(tmp_path):
    skills = tmp_path / "skills"
    agents = tmp_path / "agents"
    install = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(ROOT / "install.ps1"),
            "-Target",
            "claude",
            "-SkillDir",
            str(skills),
            "-AgentDir",
            str(agents),
            "-Source",
            "local",
            "-RepoDir",
            str(ROOT),
            "-NoDeps",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert install.returncode == 0, install.stdout + install.stderr
    assert (skills / "ads" / "SKILL.md").is_file()
    assert (skills / ".claude-ads-claude.manifest.json").is_file()

    unrelated = skills / "ads-weather"
    unrelated.mkdir()
    unrelated.joinpath("SKILL.md").write_text("user-owned\n", encoding="utf-8")
    uninstall = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(ROOT / "uninstall.ps1"),
            "-Target",
            "claude",
            "-SkillDir",
            str(skills),
            "-AgentDir",
            str(agents),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert uninstall.returncode == 0, uninstall.stdout + uninstall.stderr
    assert not (skills / "ads" / "SKILL.md").exists()
    assert unrelated.joinpath("SKILL.md").read_text(encoding="utf-8") == "user-owned\n"
