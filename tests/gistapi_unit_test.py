def test_request_example(client):
    response = client.get("/ping")
    assert response.data == b"pong"