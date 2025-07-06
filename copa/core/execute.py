import typer
import yaml
import importlib
import ansible_runner
from pathlib import Path
from typing import Dict, Any, List, Union


# TODO: move exception catching out to cli and tui

def run_ansible_playbook(playbook_path: str):
    """Execute an Ansible playbook using ansible-runner."""
    result = ansible_runner.run(
        playbook=playbook_path,
        inventory={'localhost': {'ansible_connection': 'local'}}
    )
    if result.status == 'successful':
        typer.echo(f"✓ Successfully ran {playbook_path}")
    else:
        typer.echo(f"✗ Failed to run {playbook_path}", err=True)
        raise typer.Exit(code=1)


def run_python_function(module_path: str):
    """Import and execute a Python function."""
    parts = module_path.split('.')
    function_name = parts[-1]
    module_path = '.'.join(parts[:-1])
    
    try:
        module = importlib.import_module(module_path)
        func = getattr(module, function_name)
        func()
        typer.echo(f"✓ Successfully executed {module_path}.{function_name}")
    except Exception as e:
        typer.echo(f"✗ Failed to execute {module_path}.{function_name}: {e}", err=True)
        raise typer.Exit(code=1)
