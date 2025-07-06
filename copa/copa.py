""" copa version < 1.0 only includes a CLI. TUI available from version 1.0+ """
from .cli import app


def main():
    # Alls request currently go to the CLI
    app()


if __name__ == "__main__":
    main()


"""copa launcher module.

This module launches either the CLI or the TUI interface for copa.
the availability Versions < 1.0 only support CLI, 
while TUI is available from version 1.0+.
"""

import logging
import sys
from .cli import app as cli_app
from .tui import run_tui  # Assume TUI entry point is called `run_tui`

logging.basicConfig(level=logging.INFO)
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
        logger.info("Launching CLI mode...")
        cli_app()
    else:
        logger.info("No command-line arguments detected. Launching TUI mode...")
        run_tui()


if __name__ == "__main__":
    main()
