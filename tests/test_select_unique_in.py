import altpacom.altpacom as apc


def test_select_unique_in(responses):
    p10 = responses["p10"]["packages"]
    p10_names = {p["name"] for p in p10}

    sisyphus = responses["sisyphus"]["packages"]
    sisyphus_names = {p["name"] for p in sisyphus}

    unique_in_p10 = apc.select_unique_in(
        "p10",
        {"p10": p10, "sisyphus": sisyphus},
    )
    for p in unique_in_p10:
        assert p["name"] not in sisyphus_names

    unique_in_sisyphus = apc.select_unique_in(
        "sisyphus",
        {"p10": p10, "sisyphus": sisyphus},
    )
    for p in unique_in_sisyphus:
        assert p["name"] not in p10_names
