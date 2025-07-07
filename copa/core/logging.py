# SPDX-License-Identifier: Apache-2.0

"""Logging configuration module for the application.

Set up logging once at the app entry point using setup_logging(), 
then use logging throughout the codebase as needed.

Usage in modules:
    import logging
    logger = logging.getLogger(__name__)

    # Standard logging (e.g. info, warning, error)
    logger.info("Running something")

    # Logging exception messages and traceback:
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Divide by zero")

Note:
    Log levels:
        - CRITICAL (50): Serious errors that may prevent the program from continuing
        - ERROR (40): Failures to a process that don't stop the whole program
        - WARNING (30): Something unexpected happened or potential issues
        - INFO (20): General information about program execution
        - DEBUG (10): Debug messages used during development

    Do not call logging.basicConfig() or reconfigure logging outside the entry point.
"""
import logging
from pathlib import Path
from typing import Optional

from copa import get_or_create_config_path, TOOL_NAME


def setup_logging(verbosity: int = 0, log_to_file: Optional[Path] = None) -> None:
    """Configure logging for the application.
    
    Sets up either console or file logging handlers with appropriate log levels
    based on verbosity. File logging always logs at DEBUG level, while console
    logging respects the verbosity setting.
    
    Args:
        verbosity: Logging verbosity level.
            0 (default): ERROR and CRITICAL only
            1: WARNING, ERROR, and CRITICAL
            2: INFO, WARNING, ERROR, and CRITICAL
            3: DEBUG, INFO, WARNING, ERROR, and CRITICAL
        log_to_file: Path to the log file. If None, logs to stderr. Defaults to None.
        
    Side Effects:
        - Creates log directory if it doesn't exist (if file logging enabled)
        - Configures the root logger with console and/or file handlers
        - Overwrites any existing logging configuration
        
    Example:
        >>> setup_logging()  # ERROR and CRITICAL to stderr
        >>> setup_logging(verbosity=2)  # INFO and above to stderr
        >>> setup_logging(verbosity=3, log_to_file=Path('/tmp/myapp.log'))  # DEBUG and above to file
    """
    # Determine console log level based on verbosity
    if verbosity >= 3:
        console_level = logging.DEBUG
    elif verbosity == 2:
        console_level = logging.INFO
    elif verbosity == 1:
        console_level = logging.WARNING
    else:
        console_level = logging.ERROR
    
    # Create handlers list
    handlers: list[logging.Handler] = []
    
    if log_to_file is None:
        # Console handler only
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(logging.Formatter(
            "%(levelname)s: %(message)s"
        ))
        handlers.append(console_handler)
        log_path = None
    else:
        # File handler only
        log_path = Path(log_to_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)  # Always log everything to file
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        ))
        handlers.append(file_handler)
    
    # Configure root logger
    logging.basicConfig(
        level=logging.DEBUG,  # Set to DEBUG so handlers can filter as needed
        handlers=handlers,
        force=True  # Python 3.8+ - reconfigure even if already configured
    )
    
    # Log initial setup message
    logger = logging.getLogger(__name__)
    logger.debug(f"Logging configured with verbosity={verbosity}, log_to_file={log_to_file}")
    if log_path is not None:
        logger.debug(f"Log file: {log_path}")


def get_log_path() -> Optional[Path]:
    """Get the current log file path.
    
    Returns:
        Path to the log file if file logging is configured, None otherwise.
        
    Example:
        >>> log_path = get_log_path()
        >>> if log_path:
        ...     print(f"Logs are being written to: {log_path}")
    """
    for handler in logging.root.handlers:
        if isinstance(handler, logging.FileHandler):
            return Path(handler.baseFilename)
    return None
