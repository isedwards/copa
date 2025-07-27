# Python Functions

`copa` can execute Python functions directly, allowing you to integrate custom logic alongside Ansible playbooks.

## Function Integration

Commands in `toc.yml` that don't end in `.yml` or `.yaml` are treated as Python module.function references:

```yaml
commands:
  - monitoring:
    - health: monitoring.health_check
    - metrics: monitoring.collect_metrics
  - reporting:
    - daily: reports.generate_daily_report
```

## Function Requirements

### Module Structure
Functions must be importable from copa's execution context:

```python
# monitoring.py
import logging

logger = logging.getLogger(__name__)

def health_check():
    """Check application health status."""
    logger.info("Starting health check")
    
    # Your health check logic here
    services = ["web", "database", "cache"]
    status = {}
    
    for service in services:
        status[service] = check_service_status(service)
    
    logger.info(f"Health check complete: {status}")
    return status

def check_service_status(service_name):
    """Check if a specific service is running."""
    # Implementation here
    return "healthy"
```

### Function Signatures
Functions can accept various parameter types:

```python
def deploy_application(version="latest", environment="staging"):
    """Deploy application with specified version."""
    pass

def process_data(*args, **kwargs):
    """Process data with flexible arguments."""
    pass
```

## Logging Integration

Use Python's standard logging module - `copa` will capture and format the output:

```python
import logging

logger = logging.getLogger(__name__)

def example_function():
    logger.debug("Debug information")
    logger.info("General information")
    logger.warning("Warning message")
    logger.error("Error occurred")
    logger.critical("Critical failure")
```

Logging output respects Copa's verbosity levels:
- Default: ERROR and CRITICAL only
- '-v': WARNING and above
- `-vv`: INFO and above
- `-vvv`: DEBUG and above

## Error Handling

Handle errors gracefully in your functions:

```python
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def robust_function() -> Dict[str, Any]:
    """Example of proper error handling."""
    try:
        # Your logic here
        result = perform_operation()
        logger.info("Operation completed successfully")
        return {"status": "success", "data": result}
        
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        return {"status": "error", "message": str(e)}
        
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        raise  # Re-raise for Copa to handle
```

## Return Values

Functions can return various types of data:

```python
def get_status():
    """Return simple status."""
    return "operational"

def get_metrics():
    """Return structured data."""
    return {
        "cpu_usage": 45.2,
        "memory_usage": 67.8,
        "disk_usage": 23.1
    }

def generate_report():
    """Return nothing (side effects only)."""
    # Write report to file
    with open("report.txt", "w") as f:
        f.write("Report content")
    # No return value needed
```

## Integration with Ansible

Functions can complement Ansible playbooks:

```python
import subprocess
import json

def prepare_inventory():
    """Generate dynamic inventory for Ansible."""
    inventory = {
        "web_servers": {
            "hosts": discover_web_servers()
        },
        "db_servers": {
            "hosts": discover_db_servers()
        }
    }
    
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)
    
    return inventory

def post_deployment_checks():
    """Run checks after Ansible deployment."""
    # Verify services are running
    # Check application endpoints
    # Send notifications
    pass
```

## Best Practices

### Module Organization
```
copa/
├── functions/
│   ├── __init__.py
│   ├── monitoring.py
│   ├── deployment.py
│   └── reporting.py
└── conf/
    └── toc.yml
```

### Documentation
Use Google-style docstrings:

```python
def deploy_service(service_name: str, version: str = "latest") -> bool:
    """Deploy a service to the specified version.
    
    Args:
        service_name: Name of the service to deploy
        version: Version to deploy (defaults to 'latest')
        
    Returns:
        True if deployment succeeded, False otherwise
        
    Raises:
        ValueError: If service_name is invalid
        DeploymentError: If deployment fails
    """
    pass
```

### Type Hints
Use type hints for better code clarity:

```python
from typing import List, Dict, Optional, Union

def process_hosts(hosts: List[str]) -> Dict[str, str]:
    """Process a list of hostnames."""
    pass

def get_config(key: str) -> Optional[Union[str, int, bool]]:
    """Get configuration value."""
    pass
```

### Testing
Write tests for your functions:

```python
# tests/test_monitoring.py
import pytest
from monitoring import health_check

def test_health_check():
    """Test health check function."""
    result = health_check()
    assert isinstance(result, dict)
    assert "web" in result
    assert "database" in result
```