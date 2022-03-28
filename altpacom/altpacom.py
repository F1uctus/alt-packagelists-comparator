import json
import logging as log
import urllib.parse
from typing import Dict, Optional, List, Any, Set
from urllib.error import URLError, HTTPError
from urllib.request import urlopen

from altpacom.constants import PACKAGES_BY_PLATFORM_URL, SUPPORTED_PLATFORMS

PackageInfo = Dict[str, Any]


def load_package_list(*, platform: str, arch: Optional[str] = None) -> Dict:
    """
    Retrieves the package list from the basealt database REST API.

    :param platform: One of supported platforms.
    :param arch: One of platform's architectures.
    :return: Downloaded JSON dictionary of structure
             {"request_args": {}, "length": 1, "packages": [PackageInfo]}.
    """

    if platform not in SUPPORTED_PLATFORMS:
        log.warning(f"Unsupported platform specified: {platform}")

    target_url = PACKAGES_BY_PLATFORM_URL.format(platform)
    if arch is not None:
        target_url += "?" + urllib.parse.urlencode({"arch": arch})

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
            f"Failed to load the package list for platform: {platform}", exc_info=e
        )
        exit(e.errno)


def _group_by_name(package_list: List[PackageInfo]) -> Dict[str, PackageInfo]:
    return {pkg["name"]: pkg for pkg in package_list}


def select_unique_in(
    platform: str,
    package_lists: Dict[str, List[PackageInfo]],
) -> Set[PackageInfo]:
    """
    Finds packages unique for given platform in given platform package lists.

    :param platform: Platform to get unique packages for.
    :param package_lists: Dictionary of [Platform name] -> [Packages list]
    """

    result = _group_by_name(package_lists[platform])

    for p, package_list in package_lists.items():
        if p == platform:
            continue

        another_pl = _group_by_name(package_list)
        result = {k: result[k] for k in set(result) - set(another_pl)}

    return result.values()  # noqa


def select_newest_in(
    platform: str,
    package_lists: Dict[str, List[PackageInfo]],
) -> Set[PackageInfo]:
    """
    Finds packages of given platform that have their version greater
    than the same packages from other platform package lists specified.

    :param platform: Platform to get the newest packages for.
    :param package_lists: Dictionary of [Platform name] -> [Packages list]
    """

    common = _group_by_name(package_lists[platform])

    for p, package_list in package_lists.items():
        if p == platform:
            continue

        another_pl = _group_by_name(package_list)
        common = {
            k: common[k]
            for k in set(common) & set(another_pl)
            if common[k]["version"] > another_pl[k]["version"]
        }

    return common.values()  # noqa
