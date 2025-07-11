# SPDX-License-Identifier: MIT
"""Console script for copa"""
import logging
import sys
import typer

from copa.core.logging import get_logging_level, setup_logging
from copa.core.toc import ConfigLoadError, load_toc
from copa.core.typer import register_commands


# Error: Failed to load configuration file.
# See the log file at ~/.copa/copa.log or run with --verbose for more details.

app = typer.Typer()

@app.command()
def run(
    verbosity: int = typer.Option(
        0,
        "--verbose", "-v",
        count=True,
        help="Increase verbosity (-v, -vv for more detail)"
    )
):
    # Convert count-based verbosity to logging level
    if verbosity >= 2:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    
    setup_logging(verbosity=level)

    logger = logging.getLogger(__name__)
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")

    typer.echo("Command completed.")

# Setup initial logging
setup_logging()

app = typer.Typer()


@app.command()
def main():
    """Console script for copa."""
    typer.echo("Replace this message by putting your code into "
               "copa.cli.main")
    typer.echo("See typer documentation at https://typer.tiangolo.com/")

    config = load_toc()
    # Register all commands
    register_commands(app, config['commands'])
