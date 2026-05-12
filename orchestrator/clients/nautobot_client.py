"""
Nautobot REST API client functions.
"""

import os
from typing import Dict, List
from dotenv import load_dotenv
from orchestrator.clients.api_client import api_get
from orchestrator.parsers.nautobot_parsers import (
    build_device_object,
    extract_hostname,
    extract_platform,
    extract_platform_url,
    extract_primary_ip_url,
)


load_dotenv()

NAUTOBOT_URL = os.getenv("NAUTOBOT_URL")
NAUTOBOT_TOKEN = os.getenv("NAUTOBOT_TOKEN")


def get_devices(target_devices: List[str]) -> List[Dict]:
    """
    Retrieve selected devices from Nautobot and
    transform them into Nornir-compatible format.

    Args:
        target_devices (List[str]):
            List of target device names.

    Returns:
        List[Dict]:
            Nornir-compatible device inventory.
    """

    url = f"{NAUTOBOT_URL}/api/dcim/devices/"

    headers = {
        "Authorization": f"Token {NAUTOBOT_TOKEN}",
        "Content-Type": "application/json",
    }

    data = api_get(
        url=url,
        headers=headers,
    )

    devices = []

    for device in data.get("results", []):

        if device.get("name") not in target_devices:
            continue

        ip_url = extract_primary_ip_url(device)

        if not ip_url:
            continue

        ip_data = api_get(
            url=ip_url,
            headers=headers,
        )

        hostname = extract_hostname(ip_data)

        if not hostname:
            continue

        platform_url = extract_platform_url(device)

        if not platform_url:
            continue

        platform_data = api_get(
            url=platform_url,
            headers=headers,
        )

        platform = extract_platform(platform_data)

        if not platform:
            continue

        devices.append(
            build_device_object(
                name=device.get("name"),
                hostname=hostname,
                platform=platform,
            )
        )

    return devices