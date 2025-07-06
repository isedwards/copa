""" Read toc.yml - currently assumes toc.yml is in the copa package """
import logging
import yaml
from importlib.resources import files
from pathlib import Path

logger = logging.getLogger(__name__)


class ConfigLoadError(Exception):
    """Raised when configuration could not be loaded or parsed."""
    pass


def load_toc() -> dict:
    """
    Load the 'toc.yml' file from the 'conf' directory inside the 'copa' package.

    Returns:
        dict: Parsed YAML contents of toc.yml

    Raises:
        FileNotFoundError: If the file is missing.
        yaml.YAMLError: If the file cannot be parsed.
    """
    toc_path: Path = files("copa") / "conf" / "toc.yml"
    logger.debug(f"Attempting to load TOC from: {toc_path}")

    if not toc_path.is_file():
        raise FileNotFoundError("Could not find 'conf/toc.yml' in the 'copa' package.")

    try:
        with toc_path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Failed to parse toc.yml: {e}")
