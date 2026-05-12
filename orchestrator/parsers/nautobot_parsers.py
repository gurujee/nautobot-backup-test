"""
Nautobot response parsing functions.
"""

from typing import Dict


def extract_primary_ip_url(device: Dict) -> str:
    """
    Extract primary IPv4 URL from Nautobot device object.

    Args:
        device (Dict):
            Nautobot device object.

    Returns:
        str:
            Primary IPv4 URL.
    """

    primary_ip4 = device.get("primary_ip4")

    if not primary_ip4:
        return ""

    return primary_ip4.get("url", "")


def extract_platform_url(device: Dict) -> str:
    """
    Extract platform URL from Nautobot device object.

    Args:
        device (Dict):
            Nautobot device object.

    Returns:
        str:
            Platform URL.
    """

    platform = device.get("platform")

    if not platform:
        return ""

    return platform.get("url", "")


def extract_hostname(ip_data: Dict) -> str:
    """
    Extract hostname/IP value from Nautobot IP object.

    Args:
        ip_data (Dict):
            Nautobot IP object.

    Returns:
        str:
            IPv4 host address.
    """

    return ip_data.get("host", "")


def extract_platform(platform_data: Dict) -> str:
    """
    Extract network driver from Nautobot platform object.

    Args:
        platform_data (Dict):
            Nautobot platform object.

    Returns:
        str:
            Network driver.
    """

    return platform_data.get("network_driver", "")


def build_device_object(
    name: str,
    hostname: str,
    platform: str,
) -> Dict:
    """
    Build Nornir-compatible device object.

    Args:
        name (str):
            Device name.

        hostname (str):
            Device hostname/IP.

        platform (str):
            Network driver.

    Returns:
        Dict:
            Nornir-compatible device object.
    """

    return {
        "name": name,
        "hostname": hostname,
        "platform": platform,
    }