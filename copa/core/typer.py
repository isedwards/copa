# SPDX-License-Identifier: MIT
import typer
from typing import Dict, Any, List

from copa.core.execute import run_ansible_playbook, run_python_function


def create_command_handler(target: str, help_text: str = None):
    """Create a command handler for either Ansible playbook or Python function.
    
    Args:
        target: Path to playbook or module.function reference
        help_text: Optional help text for the command
    """
    def handler():
        if target.endswith('.yml') or target.endswith('.yaml'):
            run_ansible_playbook(target)
        else:
            run_python_function(target)
    
    # Set docstring for help display (since function is dynamically created, 
    # we can't use a normal docstring and must assign to __doc__ instead)
    if help_text:
        handler.__doc__ = help_text
    
    return handler


# TODO: pass in app from cli.py

def register_commands(app: typer.Typer, commands: List[Dict[str, Any]], prefix: str = ""):
    """Recursively register commands from the configuration dictionary."""
    for command_dict in commands:
        for cmd_name, cmd_value in command_dict.items():
            full_cmd_name = f"{prefix}{cmd_name}" if prefix else cmd_name

            if isinstance(cmd_value, str):
                # Direct command pointing to a file or function
                # Parse optional help text after comma
                parts = cmd_value.split(',', 1)
                target = parts[0].strip()
                help_text = parts[1].strip() if len(parts) > 1 else None
                
                handler = create_command_handler(target, help_text)
                app.command(name=cmd_name)(handler)

            elif isinstance(cmd_value, list):
                # Subcommand group
                sub_app = typer.Typer()
                app.add_typer(sub_app, name=cmd_name)
                register_commands(sub_app, cmd_value, prefix=f"{full_cmd_name}.")

            elif isinstance(cmd_value, dict):
                # Nested commands
                sub_app = typer.Typer()
                app.add_typer(sub_app, name=cmd_name)
                # Convert dict to list format for recursive processing
                sub_commands = [{k: v} for k, v in cmd_value.items()]
                register_commands(sub_app, sub_commands, prefix=f"{full_cmd_name}.")
