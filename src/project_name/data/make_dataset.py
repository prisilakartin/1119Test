"""Helpers for creating project datasets."""

from pathlib import Path


def ensure_data_directories(root: str | Path = ".") -> None:
    """Create the standard data directories if they do not exist."""
    root = Path(root)
    for name in ("raw", "interim", "processed", "external"):
        (root / "data" / name).mkdir(parents=True, exist_ok=True)
