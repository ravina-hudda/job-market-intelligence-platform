import yaml
from pathlib import Path


def load_yaml(file_path: str) :
    """
    Load data from YAML configuration file.

    Args:
        file_path: Path to the YAML file

    Returns:
        Dictionary containing the loaded configuration data

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValueError: If YAML is invalid
    """

    file_path = Path(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Configuration file not found: {file_path}"
        )

    except yaml.YAMLError as e:
        raise ValueError(
            f"Invalid YAML format in {file_path}: {e}"
        )

    if not config:
        raise ValueError(
            f"Configuration file is empty: {file_path}"
        )

    return config