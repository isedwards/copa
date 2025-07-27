# Configuration

`copa` uses a YAML configuration file to define your available commands and their implementations.

## Configuration File Location

The configuration file is located at:
```
copa/conf/toc.yml
```

## Basic Structure

```yaml
commands:
  - command_name:
    - subcommand1: path/to/playbook.yml
    - subcommand2: module.function_name
    - subcommand3: another/playbook.yaml
```

## Command Types

### Ansible Playbooks

Files ending in `.yml` or `.yaml` are executed as Ansible playbooks:

```yaml
commands:
  - deploy:
    - web: playbooks/deploy-web.yml
    - database: playbooks/deploy-db.yml
```

Usage:
```bash
copa deploy web
copa deploy database
```

### Python Functions

Other strings are treated as Python module.function references:

```yaml
commands:
  - status:
    - check: monitoring.health_check
    - report: reporting.generate_report
```

Usage:
```bash
copa status check
copa status report
```

## Nested Commands

You can create deeply nested command structures:

```yaml
commands:
  - infrastructure:
    - aws:
      - ec2: playbooks/aws/ec2.yml
      - rds: playbooks/aws/rds.yml
    - azure:
      - vm: playbooks/azure/vm.yml
```

Usage:
```bash
copa infrastructure aws ec2
copa infrastructure azure vm
```

## Example Configuration

Here's a complete example:

```yaml
commands:
  - application:
    - deploy: playbooks/deploy.yml
    - rollback: playbooks/rollback.yml
    - status: app.status.check_health
  - infrastructure:
    - provision: playbooks/provision.yml
    - destroy: playbooks/destroy.yml
  - monitoring:
    - setup: playbooks/monitoring.yml
    - alerts: monitoring.setup_alerts
```

## Configuration Validation

Copa validates your configuration on startup. Common errors:

- **Missing files**: Playbook files that don't exist
- **Invalid modules**: Python modules that can't be imported
- **Syntax errors**: Invalid YAML syntax
