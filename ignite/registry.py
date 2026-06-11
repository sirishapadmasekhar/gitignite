from ignite.detectors.node_detector import detect_node
from ignite.detectors.python_detector import detect_python
from ignite.rules.node import NODE_IGNORE_RULES
from ignite.rules.python import PYTHON_IGNORE_RULES
from ignite.detectors.vscode_detector import detect_vscode
from ignite.rules.vscode import VSCODE_IGNORE_RULES
from ignite.detectors.jupyter_detector import detect_jupyter
from ignite.rules.jupyter import JUPYTER_IGNORE_RULES
TECHNOLOGIES = [
    {
        "name": "Python",
        "detector": detect_python,
        "rules": PYTHON_IGNORE_RULES,
    },
    {
        "name": "Node.js",
        "detector": detect_node,
        "rules": NODE_IGNORE_RULES,
    },
    {
    "name": "VS Code",
    "detector": detect_vscode,
    "rules": VSCODE_IGNORE_RULES,
},
{
    "name": "Jupyter",
    "detector": detect_jupyter,
    "rules": JUPYTER_IGNORE_RULES,
},
]