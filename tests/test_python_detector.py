from ignite.detectors.python_detector import detect_python


def test_detect_python_with_pyproject(tmp_path):
    (tmp_path / "pyproject.toml").touch()

    assert detect_python(tmp_path) is True


def test_detect_python_without_markers(tmp_path):
    assert detect_python(tmp_path) is False