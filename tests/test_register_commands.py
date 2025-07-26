# SPDX-License-Identifier: MIT

"""Tests for copa command registration"""

import typer

from copa.core.typer import register_commands


def test_register_commands_with_help_text():
    """Test register_commands with help text provided."""
    app = typer.Typer()
    commands = [
        {"install": [
            {"app": "test.yml, Install and configure application"}
        ]}
    ]
    
    register_commands(app, commands)
    
    # Check that the command was registered
    assert len(app.registered_groups) == 1
    install_group = app.registered_groups[0]
    assert install_group.name == "install"
    
    # Check that the subcommand has help text
    install_app = install_group.typer_instance
    assert len(install_app.registered_commands) == 1
    app_command = install_app.registered_commands[0]
    assert app_command.name == "app"
    assert app_command.callback.__doc__ == "Install and configure application"


def test_register_commands_without_help_text():
    """Test register_commands without help text."""
    app = typer.Typer()
    commands = [
        {"install": [
            {"app": "test.yml"}
        ]}
    ]
    
    register_commands(app, commands)
    
    # Check that the command was registered
    assert len(app.registered_groups) == 1
    install_group = app.registered_groups[0]
    assert install_group.name == "install"
    
    # Check that the subcommand has no custom help text
    install_app = install_group.typer_instance
    assert len(install_app.registered_commands) == 1
    app_command = install_app.registered_commands[0]
    assert app_command.name == "app"
    assert app_command.callback.__doc__ is None