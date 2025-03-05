from bdd_helper import *
from gistapi.app_logic import filter


def test_extract_matches():
    Given("regex and gist")
    pattern="LLM.*dy"
    gists=[
        {
            "description":"LLM study"
        },
        {
            "description": "VM study"
        },
    ]

    When("filter")
    filtered=filter(gists,pattern)

    Then("is expected")
    assert len(filtered) == 1

