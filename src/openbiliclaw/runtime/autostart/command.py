"""Resolve the backend launch command used by OS autostart entries."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING

from openbiliclaw.config import _project_root

from .base import LaunchSpec

if TYPE_CHECKING:
    from openbiliclaw.config import Config


def build_launch_spec(config: Config) -> LaunchSpec:
    """Build the stable backend command embedded in OS autostart entries."""
    del config  # The signature stays manager-friendly as config-driven fields grow.
    working_dir = _project_root()
    return LaunchSpec(
        argv=[sys.executable, "-m", "openbiliclaw.cli", "start"],
        working_dir=working_dir,
        env={
            "OPENBILICLAW_PROJECT_ROOT": str(working_dir),
        },
    )


def resolve_pythonw(executable: str | Path | None = None) -> Path:
    """Return pythonw.exe next to ``executable`` when present, else the executable."""
    python = Path(executable) if executable is not None else Path(sys.executable)
    pythonw = python.with_name("pythonw.exe")
    return pythonw if pythonw.exists() else python
