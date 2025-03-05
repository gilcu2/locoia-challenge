from bdd_helper import *

def test_search(client):
    Given("input")
    input = {"username": "gilcu2", "pattern": ".*"}

    When("get search")
    response = client.post("/api/v1/search", json=input)

    Then("it is expected")
    assert response.status_code == 200
    result = response.json
    assert result["status"] == "success"
    assert len(result["matches"]) > 0

