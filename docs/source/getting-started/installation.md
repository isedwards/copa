# Installation

## Requirements

- Python 3.8 or higher
- pip package manager

## Install from Source

Clone the repository and install in development mode:

```bash
git clone https://github.com/open-climate/copa_development.git
cd copa_development/copa
pip install -e .
```

## Dependencies

Copa automatically installs these dependencies:

- **ansible** - For playbook execution
- **ansible-runner** - Ansible execution interface
- **pyyaml** - YAML configuration parsing
- **textual** - Future TUI support
- **typer** - CLI framework

## Optional Dependencies

For development:
```bash
pip install -e .[dev]
```

For building documentation:
```bash
pip install -e .[docs]
```

For both:
```bash
pip install -e .[dev,docs]
```

## Verify Installation

Check that Copa is installed correctly:

```bash
copa --help
```

You should see the Copa CLI help output.