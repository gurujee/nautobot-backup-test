"""
Inventory loader functions.
"""

from typing import List

import yaml


def load_target_devices(file_path: str) -> List[str]:
    """
    Load target device names from YAML inventory file.

    Args:
        file_path (str):
            Path to YAML inventory file.

    Returns:
        List[str]:
            List of target device names.
    """

    with open(file_path, "r", encoding="utf-8") as file:

        data = yaml.safe_load(file)

    return data["devices"]