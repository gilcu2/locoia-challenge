from bdd_helper import *


def test_ping(client):
    Given("client")

    When("get ping")
    response = client.get("/ping")

    Then("it is expected")
    assert response.data == b"pong"