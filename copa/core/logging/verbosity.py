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


def get_logging_level(args: list[str]) -> int:
    """Get logging level from command line arguments.

    ERROR and CRITICAL levels are always reported. Additional logs can be 
    returned by specifying verbosity options:
    
    - Count-based: -v (≥WARNING), -vv (≥INFO), -vvv (≥DEBUG)
    - Level-based: --verbosity=info, --verbosity=debug  
    - Numeric: --verbosity=2 (equivalent to ≥INFO)
    
    Args:
        args: Command line arguments to parse.
        
    Returns:
        Python logging level constant. ERROR (40) by default, WARNING (30), 
        INFO (20), or DEBUG (10) based on verbosity settings.
        
    Examples:
        >>> get_logging_level(['-v'])
        logging.WARNING
        >>> get_logging_level(['-vv']) 
        logging.INFO
        >>> get_logging_level(['--verbosity=info'])
        logging.INFO
        >>> get_logging_level(['--verbosity=debug'])
        logging.DEBUG
        >>> get_logging_level(['--verbosity=2'])
        logging.INFO
    """    
    # Users may specify verbosity levels using either count-based or the following level-based arguments.
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
