"""
Nornir API client functions.
"""

import requests


def run_command(
    devices,
    command,
    textfsm=False,
):
    """
    Execute command via Nornir API.
    """

    url = "http://10.255.1.51:5000/run"

    payload = {
        "devices": devices,
        "command": command,
        "textfsm": textfsm,
    }

    response = requests.post(
        url=url,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    return response.json()