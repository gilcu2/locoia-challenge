from bdd_helper import Given, Then, When
from gistapi.github_calls import get_gists, download_whole_file


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

# TODO need a large file example
def test_download_whole_file():
    Given("gist file")
    gist_file = get_gists(per_page=1)[0].files[0]

    When("download ")
    r = download_whole_file(gist_file)

    Then("result is expected")
    assert len(r.text) == r.size
