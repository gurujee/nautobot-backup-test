"""
Generic REST API helper functions.
"""

from typing import Dict
import requests

def api_get(url: str, headers: Dict) -> Dict:
    """
    Execute HTTP GET request.

    Args:
        url (str):
            Target API URL.

        headers (Dict):
            HTTP headers.

    Returns:
        Dict:
            JSON response body.
    """

    response = requests.get(
        url=url,
        headers=headers,
        verify=False,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()