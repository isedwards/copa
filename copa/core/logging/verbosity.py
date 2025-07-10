# SPDX-License-Identifier: MIT
import argparse
import sys
from typing import Union


def get_verbosity(args: list[str] = None) -> int:
    """Get verbosity level from command line arguments.
    
    Supports multiple verbosity formats:
    - Count-based: -v, -vv, -vvv (returns 1, 2, 3)
    - Level-based: --verbosity=info, --verbosity=debug (returns corresponding level)
    - Numeric: --verbosity=2 (returns 2)
    
    Args:
        args: Command line arguments to parse. If None, uses sys.argv[1:]
        
    Returns:
        int: Verbosity level (0=error, 1=warning, 2=info, 3=debug)
        
    Examples:
        >>> get_verbosity(['-v'])
        1
        >>> get_verbosity(['-vv'])
        2
        >>> get_verbosity(['--verbosity=info'])
        2
        >>> get_verbosity(['--verbosity=debug'])
        3
        >>> get_verbosity(['--verbosity=2'])
        2
    """
    if args is None:
        args = sys.argv[1:]
    
    # Level name to number mapping
    level_map = {
        'error': 0,
        'warning': 1,
        'warn': 1,
        'info': 2,
        'debug': 3
    }
    
    parser = argparse.ArgumentParser(add_help=False)
    
    # Count-based verbosity (-v, -vv, -vvv)
    parser.add_argument('-v', '--verbose', action='count', default=0, dest='count_verbosity')
    
    # Level-based verbosity (--verbosity=info, --verbosity=2)
    parser.add_argument('--verbosity', type=str, default=None, dest='level_verbosity')
    
    # Parse only known args to avoid conflicts with other parsers
    parsed_args, _ = parser.parse_known_args(args)
    
    # Start with count-based verbosity
    verbosity = parsed_args.count_verbosity
    
    # Override with level-based verbosity if provided
    if parsed_args.level_verbosity is not None:
        level_str = parsed_args.level_verbosity.lower()
        
        # Try to parse as level name first
        if level_str in level_map:
            verbosity = level_map[level_str]
        else:
            # Try to parse as number
            try:
                verbosity = int(level_str)
            except ValueError:
                # Invalid verbosity level, default to 0
                verbosity = 0
    
    # Clamp to valid range
    return max(0, min(verbosity, 3))


if __name__ == "__main__":
    # Test examples
    test_cases = [
        (['-v'], 1),
        (['-vv'], 2),
        (['-vvv'], 3),
        (['--verbosity=info'], 2),
        (['--verbosity=debug'], 3),
        (['--verbosity=warning'], 1),
        (['--verbosity=error'], 0),
        (['--verbosity=2'], 2),
        (['--verbosity=5'], 3),  # Clamped to max
        (['-v', '--verbosity=debug'], 3),  # Level overrides count
        (['--verbosity=invalid'], 0),  # Invalid defaults to 0
        ([], 0),  # Default
    ]
    
    for args, expected in test_cases:
        result = get_verbosity(args)
        status = "✓" if result == expected else "✗"
        print(f"{status} {args} -> {result} (expected {expected})")