# Commands

Copa's command system is built around dynamic registration from your `toc.yml` configuration file.

## How Commands Work

1. **Definition**: Commands are defined in `copa/conf/toc.yml`
2. **Loading**: Configuration is loaded at startup via `copa/core/toc.py`
3. **Registration**: Commands are dynamically registered using `copa/core/typer.py`
4. **Execution**: Commands are executed via `copa/core/execute.py`

## Command Syntax

```bash
copa <command> <subcommand> [options]
```

### Global Options

- `-v, --verbose`: Increase verbosity (can be used multiple times)
- `-q, --quiet`: Decrease verbosity
- `--help`: Show help information

### Verbosity Levels

- **0** (default): ERROR and CRITICAL only
- **1** (`-v`): WARNING and above
- **2** (`-vv`): INFO and above
- **3** (`-vvv`): DEBUG and above

## Command Discovery

List all available commands:
```bash
copa --help
```

Get help for a specific command:
```bash
copa mycommand --help
```

## Command Execution Flow

### For Ansible Playbooks

1. Copa identifies the playbook file
2. Validates the file exists
3. Executes using `ansible-runner`
4. Streams output with appropriate logging level

### For Python Functions

1. Copa imports the specified module
2. Calls the function with any provided arguments
3. Handles return values and exceptions
4. Logs execution details

## Error Handling

Copa provides comprehensive error handling:

- **Configuration errors**: Invalid `toc.yml` syntax
- **Missing files**: Playbook files that don't exist
- **Import errors**: Python modules that can't be loaded
- **Execution errors**: Runtime failures in playbooks or functions

All errors are logged with appropriate detail levels based on verbosity settings.