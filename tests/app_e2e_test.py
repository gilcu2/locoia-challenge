import requests

from bdd_helper import Given, Then, When


def test_ping():
    When("get ping")
    response = requests.get("http://localhost:8000/ping")

    Then("it is expected")
    assert response.status_code == 200
    assert response.text == '"pong"\n'


def test_search_when_user():
    Given("input")
    input = {"username": "gilcu2", "pattern": ".*"}

    When("get search")
    response = requests.post("http://localhost:8000/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "success"
    assert len(result["matches"]) > 0


def test_search_when_pagination():
    Given("input")
    input = {"page": 2, "per_page": 2}

    When("get search")
    response = requests.post("http://localhost:8000/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "success"
    assert len(result["matches"]) == 2
