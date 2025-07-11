# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Copa is a Python CLI tool that provides a unified interface for configuring, orchestrating, and provisioning applications. It's designed to work with Terraform (provisioning), Ansible (orchestration), and Python functions through a single command-line interface.

## Core Architecture

### Entry Points
- **Main Entry**: `copa/copa.py:main()` - Determines whether to launch CLI or TUI mode
- **CLI Entry**: `copa/cli.py:main()` - Typer-based CLI interface
- **Script Entry**: Configured in `pyproject.toml` as `copa = "copa.cli:main"`

### Command System
The application uses a dynamic command registration system:

1. **Configuration**: Commands are defined in `copa/conf/toc.yml`
2. **Loading**: `copa/core/toc.py:load_toc()` reads the YAML configuration
3. **Registration**: `copa/core/typer.py:register_commands()` dynamically creates Typer commands
4. **Execution**: `copa/core/execute.py` handles running Ansible playbooks or Python functions

### Key Components

- **copa/__init__.py**: Configuration path management (`get_or_create_config_path()`)
- **copa/core/logging.py**: Comprehensive logging setup with verbosity levels
- **copa/core/toc.py**: YAML configuration loading with error handling
- **copa/core/typer.py**: Dynamic command registration from configuration
- **copa/core/execute.py**: Ansible playbook and Python function execution

## Development

- Code must run on Python 3.8 (and above)
- All code must have type definitions and Google-style docstrings
- All functions with side effects must explicitly document them in their docstrings (file I/O, network calls, state changes, etc.)
- Code should have optimal logging. CRITICAL logs should be used for unexpected crashes that will terminate the application
- All Python files must have begin with the following licence line:
    # SPDX-License-Identifier: MIT 
- Avoid text that credits AI tools in the code and commit messages

### Development Commands

#### Installation
```bash
pip install -e .
```

#### Testing
```bash
pytest
```
Run individual test:
```bash
pytest tests/test_wx.py::TestWx::test_addition
```

#### Package Building
```bash
python -m build
```

## Configuration System

Commands are configured in `copa/conf/toc.yml` using this structure:
```yaml
commands:
  - command_name:
    - subcommand: path/to/playbook.yml
    - another_sub: module.function_name
```

- `.yml`/`.yaml` files are executed as Ansible playbooks
- Other strings are treated as Python module.function references
- Supports nested command structures

## Code Patterns

### Command Handler Creation
Commands are created dynamically in `copa/core/typer.py:create_command_handler()`:
- Ansible playbooks: Execute with `ansible-runner`
- Python functions: Import and call using `importlib`

### Logging Usage
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Message")
```

Logging is configured once at startup with verbosity levels:
- 0: ERROR and CRITICAL only
- 1: WARNING and above
- 2: INFO and above  
- 3: DEBUG and above

### Error Handling
- `ConfigLoadError` for configuration loading issues
- Typer's `Exit(code=1)` for command failures
- Standard Python exceptions with logging

## Project Structure

```
copa/
├── copa/
│   ├── __init__.py          # Config path utilities
│   ├── copa.py              # Main entry point
│   ├── cli.py               # CLI interface
│   ├── core/
│   │   ├── execute.py       # Ansible/Python execution
│   │   ├── logging.py       # Logging configuration
│   │   ├── toc.py           # Configuration loading
│   │   └── typer.py         # Dynamic command registration
│   └── conf/
│       └── toc.yml          # Command configuration
├── tests/
│   └── test_wx.py           # Test suite
└── pyproject.toml           # Package configuration
```

## Dependencies

- **typer**: CLI framework
- **textual**: Future TUI support (planned)
- **ansible**: Playbook execution via ansible-runner
- **pyyaml**: Configuration file parsing
- **pytest**: Testing framework

## Future Development

- TUI interface planned for v1.0+ using Textual
- Web UI support mentioned in roadmap
- Currently CLI-only in versions < 1.0