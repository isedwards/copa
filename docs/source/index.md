# copa Documentation

Welcome to `copa` - a unified CLI tool for **C**onfiguring, **O**rchestrating, and **P**rovisioning **A**pplications.

## What is Copa?

Copa provides a single command-line interface that combines:

- **Configuration Management** with Ansible and Jinja2 templating
- **Orchestration** with Ansible playbooks  
- **Provisioning** with Terraform
- **Python Function Integration** for custom logic

## Key Features

- Dynamic command registration from YAML configuration
- Seamless Ansible playbook execution with Jinja2 templating
- Python function integration
- Comprehensive logging with verbosity levels
- Extensible architecture for future TUI/Web interfaces

## Quick Example

```bash
# Install copa
pip install -e .

# Run a command (defined in toc.yml)
copa install mytool
```

## Getting Started

1. [Installation](getting-started/installation.md) - Install copa and dependencies
2. [Quick Start](getting-started/quickstart.md) - Your first copa command
3. [Configuration](getting-started/configuration.md) - Set up your `toc.yml`

## Architecture Overview

Copa uses a dynamic command system:

1. Commands defined in `copa/conf/toc.yml`
2. Main entry loads configuration via `copa/core/toc.py`
3. CLI initialization registers commands dynamically
4. Execution handles Ansible playbooks or Python functions

See the [Architecture Guide](developer-guide/architecture.md) for detailed information.
