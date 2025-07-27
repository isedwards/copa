# Quick Start

This guide will get you running your first Copa command in minutes.

## 1. Check Your Configuration

Copa uses a configuration file at `copa/conf/toc.yml` to define available commands:

```bash
cat copa/conf/toc.yml
```

## 2. Run Copa

Display available commands:

```bash
copa --help
```

This shows all commands dynamically loaded from your `toc.yml` configuration.

## 3. Command Structure

Copa commands follow this pattern:

```bash
copa <command> <subcommand> [options]
```

Where:
- `<command>` and `<subcommand>` are defined in `toc.yml`
- Commands can execute Ansible playbooks (`.yml`/`.yaml` files)
- Commands can call Python functions (`module.function_name`)

## 4. Example Command

If your `toc.yml` contains:

```yaml
commands:
  - myapp:
    - deploy: playbooks/deploy.yml
    - status: mymodule.check_status
```

You can run:

```bash
# Execute Ansible playbook
copa myapp deploy

# Call Python function
copa myapp status
```

## 5. Verbosity Levels

Control logging output:

```bash
copa myapp deploy -v      # WARNING level
copa myapp deploy -vv     # INFO level
copa myapp deploy -vvv    # DEBUG level
copa myapp deploy         # Quiet (unrecoverable errors only)
```

## Next Steps

- [Configure your commands](configuration.md)
- [Learn about playbooks](../user-guide/playbooks.md)
- [Integrate Python functions](../user-guide/python-functions.md)