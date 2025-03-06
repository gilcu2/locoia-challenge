from pytest_mock import MockFixture

from bdd_helper import And, Given, Then, When
from gistapi.app_logic import GistResult


def test_ping(client):
    Given("client")

    When("get ping")
    response = client.get("/ping")

    Then("it is expected")
    assert response.status_code == 200
    assert response.data == b'"pong"\n'


def test_search_when_ok(client, mocker: MockFixture):
    Given("input")
    username = "gilcu2"
    pattern = ".*"
    input = {"username": username, "pattern": pattern}

    And("Mocked responses")
    result = GistResult(
        status="success",
        username=username,
        pattern=pattern,
        matches=[],
        total=1,
    )
    mocker.patch("gistapi.app.get_gists", return_value=[])
    mocker.patch("gistapi.app.filter", return_value=[])
    mocker.patch("gistapi.app.create_result", return_value=result)

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    assert GistResult.model_validate(response.json) == result


def test_search_when_api_call_fails(client, mocker: MockFixture):
    Given("input")
    username = "gilcu2"
    pattern = ".*"
    input = {"username": username, "pattern": pattern}

    And("Mocked responses")
    mocker.patch("gistapi.app.get_gists", side_effect=Exception("Github problem"))

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 500


def test_swagger(client, mocker: MockFixture):
    When("get root")
    response = client.get("/")

    Then("it is expected")
    assert response.status_code == 200
    assert "Gist Search API" in response.data.decode("utf-8")
