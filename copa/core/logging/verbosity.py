# SPDX-License-Identifier: MIT
"""
  1. CRITICAL (50) - Serious error, program may be unable to continue
  2. ERROR (40) - Due to a serious problem, software couldn't perform a function
  3. WARNING (30) - Something unexpected happened or potential issue
  4. INFO (20) - General information confirming things are working
  5. DEBUG (10) - Detailed information for diagnosing problems

"""
import argparse
import logging
import sys


def get_logging_level(args: list[str] = None) -> int:
    """Get logging level from command line arguments.
    
    Supports multiple verbosity formats:
    - Count-based: -v, -vv, -vvv (returns INFO, DEBUG, DEBUG)
    - Level-based: --verbosity=info, --verbosity=debug (returns corresponding level)
    - Numeric: --verbosity=2 (returns INFO)
    
    Args:
        args: Command line arguments to parse. If None, uses sys.argv[1:]
        
    Returns:
        int: Python logging level constant (ERROR=40, WARNING=30, INFO=20, DEBUG=10)
        
    Examples:
        >>> get_logging_level(['-v'])
        30
        >>> get_logging_level(['-vv'])
        20
        >>> get_logging_level(['--verbosity=info'])
        20
        >>> get_logging_level(['--verbosity=debug'])
        10
        >>> get_logging_level(['--verbosity=2'])
        20
    """
    if args is None:
        args = sys.argv[1:]
    
    # Level name to logging constant mapping
    level_map = {
        'error': logging.ERROR,
        'warning': logging.WARNING,
        'warn': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG
    }
    
    parser = argparse.ArgumentParser(add_help=False)
    
    # Count-based verbosity (-v, -vv, -vvv)
    parser.add_argument('-v', '--verbose', action='count', default=0, dest='count_verbosity')
    
    # Level-based verbosity (--verbosity=info, --verbosity=2)
    parser.add_argument('--verbosity', type=str, default=None, dest='level_verbosity')
    
    # Parse only known args to avoid conflicts with other parsers
    parsed_args, _ = parser.parse_known_args(args)
    
    # Start with count-based verbosity
    count_verbosity = parsed_args.count_verbosity
    
    # Override with level-based verbosity if provided
    if parsed_args.level_verbosity is not None:
        level_str = parsed_args.level_verbosity.lower()
        
        # Try to parse as level name first
        if level_str in level_map:
            return level_map[level_str]
        else:
            # Try to parse as number (old custom verbosity levels)
            try:
                custom_level = int(level_str)
                # Map custom levels to logging constants
                if custom_level >= 3:
                    return logging.DEBUG
                elif custom_level == 2:
                    return logging.INFO
                elif custom_level == 1:
                    return logging.WARNING
                else:
                    return logging.ERROR
            except ValueError:
                # Invalid verbosity level, default to ERROR
                return logging.ERROR
    
    # Map count-based verbosity to logging constants
    if count_verbosity >= 3:
        return logging.DEBUG
    elif count_verbosity == 2:
        return logging.INFO
    elif count_verbosity == 1:
        return logging.WARNING
    else:
        return logging.ERROR


if __name__ == "__main__":
    # Test examples
    import logging
    test_cases = [
        (['-v'], logging.WARNING),
        (['-vv'], logging.INFO),
        (['-vvv'], logging.DEBUG),
        (['--verbosity=info'], logging.INFO),
        (['--verbosity=debug'], logging.DEBUG),
        (['--verbosity=warning'], logging.WARNING),
        (['--verbosity=error'], logging.ERROR),
        (['--verbosity=2'], logging.INFO),
        (['--verbosity=5'], logging.DEBUG),  # Clamped to max
        (['-v', '--verbosity=debug'], logging.DEBUG),  # Level overrides count
        (['--verbosity=invalid'], logging.ERROR),  # Invalid defaults to ERROR
        ([], logging.ERROR),  # Default
    ]
    
    for args, expected in test_cases:
        result = get_logging_level(args)
        status = "✓" if result == expected else "✗"
        print(f"{status} {args} -> {result} (expected {expected})")