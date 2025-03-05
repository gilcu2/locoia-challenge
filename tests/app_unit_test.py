from bdd_helper import *
from pytest_mock import MockFixture


def test_ping(client):
    Given("client")

    When("get ping")
    response = client.get("/ping")

    Then("it is expected")
    assert response.status_code == 200
    assert response.data == b"pong"


def test_search_when_ok(client, mocker: MockFixture):
    Given("input")
    username = "gilcu2"
    pattern = ".*"
    input = {"username": username, "pattern": pattern}

    And("Mocked responses")
    matches = {'status': 'success', 'username': username, 'pattern': pattern, 'matches': []}
    mocker.patch("gistapi.app.get_gists", return_value={})
    mocker.patch("gistapi.app.extract_matches", return_value=matches)

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    assert response.json == matches


def test_search_when_api_call_fails(client, mocker: MockFixture):
    Given("input")
    username = "gilcu2"
    pattern = ".*"
    input = {"username": username, "pattern": pattern}

    And("Mocked responses")
    mocker.patch("gistapi.app.get_gists",  side_effect=Exception("Github problem"))


    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 500
