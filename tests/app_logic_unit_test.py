from bdd_helper import Given, Then, When
from gistapi.app_logic import create_result, download_and_filter
from gistapi.github_calls import Gist, GistFile


def test_extract_matches():
    Given("regex and gist")
    pattern = "LLM.*dy"
    gists = [
        Gist(
            url="url1",
            files=[
                GistFile(
                    filename="1-1",
                    size=10,
                    url="file1-1",
                    text="LLM study",
                ),
                GistFile(
                    filename="1-2",
                    size=10,
                    url="file2-1",
                    text="LVM study",
                ),
            ]
        ),
        Gist(
            url="url2",
            files=[
                GistFile(
                    filename="2-1",
                    size=10,
                    url="file2-1",
                    text="LLM research",
                ),
                GistFile(
                    filename="2-2",
                    size=10,
                    url="file2-2",
                    text="LVM research",
                ),
            ]
        )
    ]

    When("filter")
    filtered = download_and_filter(gists, pattern)

    Then("is expected")
    assert len(filtered) == 1
    assert len(filtered[0].files) == 1
    assert filtered[0].files[0].text == gists[0].files[0].text


def test_create_result():
    Given("gists")
    gists = [
        Gist(
            url="url1",
            files=[
                GistFile(
                    filename="1-1",
                    size=10,
                    url="file1-1",
                    text="LLM study",
                ),
                GistFile(
                    filename="1-2",
                    size=10,
                    url="file2-1",
                    text="LVM study",
                ),
            ]
        ),
    ]

    When("create GistResult")
    r=create_result(gists,gists,".*", "gilcu2")

    Then("it is expected")
    assert r.matches == gists
