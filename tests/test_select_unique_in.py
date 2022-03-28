import altpacom.altpacom as apc


def test_select_unique_in():
    p10 = apc.load_package_list(platform="p10", arch="aarch64")["packages"]
    sisyphus = apc.load_package_list(platform="sisyphus", arch="aarch64")["packages"]

    unique_in_p10 = apc.select_unique_in(
        "p10",
        {"p10": p10, "sisyphus": sisyphus},
    )
    assert len(unique_in_p10) == 1480

    unique_in_sisyphus = apc.select_unique_in(
        "sisyphus",
        {"p10": p10, "sisyphus": sisyphus},
    )
    assert len(unique_in_sisyphus) == 1412
