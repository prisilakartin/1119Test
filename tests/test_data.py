from pathlib import Path


def test_data_directory_layout():
    """The repository includes the standard data stages."""
    root = Path(__file__).resolve().parents[1]
    for name in ("raw", "interim", "processed", "external"):
        assert (root / "data" / name).is_dir()
