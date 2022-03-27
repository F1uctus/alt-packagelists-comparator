import json
import logging as log
from typing import Dict
from urllib.error import URLError, HTTPError
from urllib.request import urlopen

from altpacom.constants import PACKAGES_BY_PLATFORM_URL, SUPPORTED_PLATFORMS


def load_package_list(*, platform: str) -> Dict:
    """
    Retrieves the package list from the basealt database REST API.

    :param platform: One of supported platforms.
    :return: Downloaded JSON dictionary.
    """
    if platform not in SUPPORTED_PLATFORMS:
        log.warning(f"Unsupported platform specified: {platform}")
    target_url = PACKAGES_BY_PLATFORM_URL.format(platform)
    log.debug(f"Retrieving data from {target_url}")
    try:
        with urlopen(target_url) as url:
            data = json.loads(url.read().decode())
            return data
    except HTTPError as e:
        log.warning(f"{target_url} returned {e.code}", exc_info=e)
        log.warning(f"Assuming no packages found for '{platform}' due to errors above")
        return {}
    except URLError as e:
        log.error(
            "Failed to load the package list for platform: {}",
            exc_info=e
        )
        exit(e.errno)
