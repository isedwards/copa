# SPDX-License-Identifier: MIT
"""Console script for copa"""
import logging
import typer

from copa.core.logging import setup_logging
from copa.core.typer import register_commands


app = typer.Typer()


def init_cli(config: dict) -> None:
    """Initialize the CLI by registering commands from configuration.
    
    Args:
        config: Configuration dictionary loaded from toc.yml
        
    Side Effects:
        - Registers dynamic commands with the Typer app
    """
    register_commands(app, config['commands'])


