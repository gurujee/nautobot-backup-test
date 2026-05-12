"""
Backup file management functions.
"""

import json
from pathlib import Path
from typing import Dict


BACKUP_DIRECTORY = Path("backups")


def save_backup(
    device_name: str,
    config_output: str,
    result_data: Dict,
) -> None:
    """
    Save device backup files.

    Args:
        device_name (str):
            Device hostname.

        config_output (str):
            Raw device configuration.

        result_data (Dict):
            Full Nornir execution result.

    Returns:
        None
    """

    BACKUP_DIRECTORY.mkdir(exist_ok=True)

    #
    # CONFIG BACKUP
    #

    device_directory = (
        BACKUP_DIRECTORY / device_name
    )

    device_directory.mkdir(exist_ok=True)

    config_file = (
        device_directory / f"{device_name}.cfg"
    )

    config_file.write_text(
        config_output,
        encoding="utf-8",
    )

    #
    # JSON BACKUP
    #

    json_file = (
    device_directory / f"{device_name}.json"
    )

    json_file.write_text(
        json.dumps(
            result_data,
            indent=4,
        ),
        encoding="utf-8",
    )