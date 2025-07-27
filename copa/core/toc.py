# SPDX-License-Identifier: MIT
""" Read toc.yml - currently assumes toc.yml is in the copa package """
import logging
import yaml
from importlib.resources import files
from pathlib import Path

logger = logging.getLogger(__name__)


class ConfigLoadError(Exception):
    """Raised when configuration could not be loaded or parsed."""
    pass


def load_toc(config_data: dict = None, config_path: Path = None) -> dict:
    """
    Load TOC configuration from data, custom path, or default location.

    Args:
        config_data: Optional configuration dictionary to use directly
        config_path: Optional custom path to toc.yml file

    Returns:
        dict: Configuration dictionary

    Raises:
        FileNotFoundError: If the file is missing.
        yaml.YAMLError: If the file cannot be parsed.
    """
    if config_data is not None:
        logger.debug("Using provided config data")
        return config_data
    
    if config_path is None:
        config_path = files("copa") / "conf" / "toc.yml"
    
    logger.debug(f"Attempting to load TOC from: {config_path}")

    if not config_path.is_file():
        raise FileNotFoundError("Could not find 'conf/toc.yml' in the 'copa' package.")

    try:
        with config_path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Failed to parse toc.yml: {e}")
