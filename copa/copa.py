# SPDX-License-Identifier: MIT
"""copa launcher module.

This module launches either the CLI or the TUI interface for copa.
NOTE: Versions < 1.0 only support CLI
"""
import logging
import sys

# from .cli import app as cli_app
# from .tui import run_tui  # Assume TUI entry point is called `run_tui`
from copa.core.logging import get_logging_level, setup_logging


# Setup initial logging until further config is determined
setup_logging(verbosity=get_logging_level(sys.argv), log_to_file=None)
logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for Copa.

    Launches the TUI if no command-line arguments are passed (i.e., only the script 
    name is present in sys.argv). Otherwise, defaults to the CLI interface.

    Side Effects:
        - May launch a CLI or TUI session in the terminal.
        - Writes logs to the configured logging output.
    """
    if len(sys.argv) > 1:
        logger.debug("Launching CLI mode...")
        #cli_app()
    else:
        #logger.debug("No command-line arguments detected. Launching TUI mode...")
        #run_tui()
        logger.debug("copa <1.0 does not support TUI. Launching CLI mode...")
        #cli_app()
