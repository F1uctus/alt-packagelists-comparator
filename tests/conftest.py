import json
from pathlib import Path

import pytest

import altpacom.altpacom as apc
from altpacom.constants import SUPPORTED_PLATFORMS

USE_CACHED_LISTS = True
CACHED_LISTS_DIR = Path(__file__).parent / "cached_lists"


@pytest.fixture(scope="session", autouse=True)
def responses():
    if not USE_CACHED_LISTS:
        for pn in SUPPORTED_PLATFORMS:
            CACHED_LISTS_DIR.mkdir(parents=True, exist_ok=True)
            with open(CACHED_LISTS_DIR / (pn + ".json"), mode="w") as f:
                json.dump(apc.load_package_list(platform=pn, arch="aarch64"), f)

    responses = {}
    for pn in SUPPORTED_PLATFORMS:
        with open(CACHED_LISTS_DIR / (pn + ".json")) as f:
            responses[pn] = json.load(f)

    yield responses
