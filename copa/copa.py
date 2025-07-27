# SPDX-License-Identifier: MIT
"""copa launcher module.

This module launches either the CLI or the TUI interface for copa.
NOTE: Versions < 1.0 only support CLI
"""
import logging
import sys

from copa.cli import init_cli, app as cli_app
# from copa.tui import init_tui, app as tui_app
from copa.core.logging import get_logging_level, setup_logging
from copa.core.toc import ConfigLoadError, load_toc


# Setup initial logging until further config is determined
setup_logging(verbosity=get_logging_level(sys.argv), log_to_file=None)
logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for Copa.

    Loads configuration from toc.yml and launches the TUI if no command-line arguments 
    are passed (i.e., only the script name is present in sys.argv). Otherwise, defaults 
    to the CLI interface.
    """
    # Warn about EOL Python versions
    if sys.version_info < (3, 9):
        logger.error(f"Python {sys.version_info.major}.{sys.version_info.minor} is end-of-life. Please upgrade to Python 3.10+")
    elif sys.version_info < (3, 10):
        logger.warning(f"Python {sys.version_info.major}.{sys.version_info.minor} reaches end-of-life in October 2025. Consider upgrading to Python 3.10+")
    
    try:
        config = load_toc()
        logger.debug("Configuration loaded successfully")
    except ConfigLoadError as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)
    
    if len(sys.argv) > 1:
        logger.debug("Launching CLI mode...")
        init_cli(config)
        cli_app()
    else:
        # logger.debug("No command-line arguments detected. Launching TUI mode...")
        # init_tui(config)
        # tui_app()
        logger.debug("copa <1.0 does not support TUI. Returning CLI help instead.")
        init_cli(config)
        cli_app(["--help"])
