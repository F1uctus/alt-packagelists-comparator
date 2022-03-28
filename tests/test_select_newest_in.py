import altpacom.altpacom as apc


def test_select_newest_in(responses):
    p10 = responses["p10"]["packages"]
    p10_name_to_version = {p["name"]: p["version"] for p in p10}

    sisyphus = responses["sisyphus"]["packages"]
    sisyphus_name_to_version = {p["name"]: p["version"] for p in sisyphus}

    newest_in_p10 = apc.select_newest_in(
        "p10",
        {"p10": p10, "sisyphus": sisyphus},
    )
    for p in newest_in_p10:
        assert p["version"] > sisyphus_name_to_version[p["name"]]

    newest_in_sisyphus = apc.select_newest_in(
        "sisyphus",
        {"p10": p10, "sisyphus": sisyphus},
    )
    for p in newest_in_sisyphus:
        assert p["version"] > p10_name_to_version[p["name"]]
