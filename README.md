# copa 

Configure, Orchestrate and Provision Applications

[![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![python3](https://img.shields.io/pypi/pyversions/copa)](https://python3statement.org/#sections50-why)

## About

`copa` is a single codebase, implemented using the Python Typer and Textual packages, that provides a Command Line Interface (CLI), Text User Interface (TUI) and Web UI for provisioning, orchestrating and configuring software on Linux servers.

`copa` is aware of environments that it can install to including:
1. [Provisioning](https://www.redhat.com/en/topics/automation/what-is-provisioning) (Terraform)
    - Infrastructure Providers (e.g. Locally [Proxmox](https://github.com/Telmate/terraform-provider-proxmox) or [VMWare](https://registry.terraform.io/providers/hashicorp/vsphere/latest). Remote: Amazon Web Services, Google Cloud Platform etc. see [supported providers](https://registry.terraform.io/search/providers))
2. [Orchestrating](https://www.redhat.com/en/topics/automation/what-is-orchestration) (Ansible)
    - Linux servers (VMs, cloud instances) 
3. [Configuration Management](https://www.redhat.com/en/topics/automation/what-is-configuration-management) (Ansible)
    - Modifing configuration for nginx, django etc.

`copa` attempts to be as minimal and extensible as possible.

## Installation

### For Users

To install from the Python Package Index (PyPI), first install [pipx](https://pipx.pypa.io/stable/installation/#installing-pipx), then:

```bash
pipx install copa
```

### For Developers

Developers may wish to clone the latest version from GitHub and install this local version in editable (-e) mode.

```bash
git clone https://github.com/open-climate/copa.git
pip install -e ./copa[dev,docs]
```

To execute all tests run: `pytest`

---
*Powered by:*
- [Terraform](https://developer.hashicorp.com/terraform) for [server provisioning](https://www.redhat.com/en/topics/automation/what-is-provisioning)
- [Ansible](https://docs.ansible.com/) for [server orchestration](https://www.redhat.com/en/topics/automation/what-is-orchestration)
- [Typer](https://github.com/fastapi/typer) (MIT) - Modern, type-hint based CLI framework that auto-generates help from function signatures
- [Textual](https://github.com/Textualize/textual) (MIT) - An application framework for building terminal user interfaces (TUI) and web user interfaces (WebUI) from the same Python codebase
- [pipx](https://pipx.pypa.io/stable/) - A way to install Python CLI's as a tool in a contained environment
