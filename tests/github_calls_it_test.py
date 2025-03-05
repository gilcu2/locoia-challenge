from bdd_helper import *
from gistapi.github_calls import *


def test_get_gists():
    Given("username and mocked get")
    username = "gilcu2"

    When("call")
    r = get_gists(username)

    Then("result is expected")
    assert len(r) == 1


def test_get_gists_pagination():
    Given("page and per_page")
    page = 2
    per_page = 2

    When("call")
    r = get_gists(page=page, per_page=per_page)

    Then("result is expected")
    assert len(r) == 2


def test_get_gists_pagination_when_no_more():
    Given("page and per_page")
    username = "gilcu2"
    page = 2
    per_page = 2

    When("call")
    r = get_gists(username, page=page, per_page=per_page)

    Then("result is expected")
    assert len(r) == 0
