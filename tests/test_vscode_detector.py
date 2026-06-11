from ignite.detectors.vscode_detector import detect_vscode


def test_detect_vscode_with_directory(tmp_path):
    (tmp_path / ".vscode").mkdir()

    assert detect_vscode(tmp_path) is True


def test_detect_vscode_with_workspace_file(tmp_path):
    (tmp_path / "project.code-workspace").touch()

    assert detect_vscode(tmp_path) is True


def test_detect_vscode_without_markers(tmp_path):
    assert detect_vscode(tmp_path) is False