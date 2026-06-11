from ignite.detectors.jupyter_detector import detect_jupyter


def test_detect_jupyter_with_notebook(tmp_path):
    (tmp_path / "analysis.ipynb").touch()

    assert detect_jupyter(tmp_path) is True


def test_detect_jupyter_without_notebooks(tmp_path):
    assert detect_jupyter(tmp_path) is False