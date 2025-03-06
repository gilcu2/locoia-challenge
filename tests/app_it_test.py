from bdd_helper import Given, Then, When


def test_search_when_user(client):
    Given("input")
    input = {"username": "gilcu2", "pattern": ".*"}

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    result = response.json
    assert result["status"] == "success"
    assert len(result["matches"]) > 0


def test_search_when_pagination(client):
    Given("input")
    input = {"page": 2, "per_page": 2}

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    result = response.json
    assert result["status"] == "success"
    assert len(result["matches"]) == 2
