from json.decoder import JSONDecodeError

import pytest

from bdd_helper import *
from gistapi.github_calls import *


def test_get_gists_when_ok(requests_mock):
    Given("username and mocked get")
    username = "gilcu2"
    data = {}
    requests_mock.get(f"https://api.github.com/users/{username}/gists", json=data)

    When("call")
    r = get_gists(username)

    Then("result is expected")
    assert r == data


def test_get_gists_when_problem(requests_mock):
    Given("username and mocked get")
    username = "gilcu2"
    data = "{123"
    requests_mock.get(f"https://api.github.com/users/{username}/gists", text=data)

    When("call must create exception")
    with pytest.raises(JSONDecodeError) as e_info:
        get_gists(username)
