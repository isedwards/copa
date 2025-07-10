# SPDX-License-Identifier: MIT
"""
copa: Configure, Orchestrate and Provision Applications

See README.md for usage examples and documentation.
"""
from pathlib import Path


## FIXME: Replace this with the flow defined in e3s/project/copa/README
TOOL_NAME = 'copa'


def get_or_create_config_path() -> Path:
    """
    Returns the full path to the configuration directory.

    Side Effects:
    - Creates the directory on the user's filesystem if it does not exist.

    """    
    conf_path = Path.home() / f'.{TOOL_NAME}'
    conf_path.parent.mkdir(parents=True, exist_ok=True)
    return conf_path
