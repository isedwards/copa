# SPDX-License-Identifier: MIT
"""Console script for copa"""
import logging
import typer

from copa.core.logging import setup_logging
from copa.core.toc import ConfigLoadError, load_toc
from copa.core.typer import register_commands


app = typer.Typer()


@app.command()
def main():
    """Console script for copa."""
    try:
        config = load_toc()
        # Register all commands
        register_commands(app, config['commands'])
    except ConfigLoadError as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to load configuration: {e}")
        raise typer.Exit(code=1)
