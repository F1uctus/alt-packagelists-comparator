from typing import Dict

import pytest

import altpacom.altpacom as apc
from altpacom import setup_logging
from altpacom.constants import SUPPORTED_PLATFORMS

setup_logging()


@pytest.mark.parametrize("platform", SUPPORTED_PLATFORMS)
def test_load_package_list_for_valid_platform(platform: str):
    result = apc.load_package_list(platform=platform)

    assert isinstance(result, Dict)


@pytest.mark.parametrize("platform", ["octopus", "9amogus", "123", "@$%#!"])
def test_load_package_list_for_invalid_platform(platform: str):
    result = apc.load_package_list(platform=platform)

    assert isinstance(result, Dict)
    assert len(result) == 0
