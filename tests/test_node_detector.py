from ignite.detectors.node_detector import detect_node


def test_detect_node_with_package_json(tmp_path):
    (tmp_path / "package.json").touch()

    assert detect_node(tmp_path) is True


def test_detect_node_without_markers(tmp_path):
    assert detect_node(tmp_path) is False