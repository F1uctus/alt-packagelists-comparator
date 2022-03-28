import altpacom.altpacom as apc


def test_select_unique_in(responses):
    p10 = responses["p10"]["packages"]
    sisyphus = responses["sisyphus"]["packages"]

    unique_in_p10 = apc.select_unique_in(
        "p10",
        {"p10": p10, "sisyphus": sisyphus},
    )
    assert len(unique_in_p10) == 1482

    unique_in_sisyphus = apc.select_unique_in(
        "sisyphus",
        {"p10": p10, "sisyphus": sisyphus},
    )
    assert len(unique_in_sisyphus) == 1412
