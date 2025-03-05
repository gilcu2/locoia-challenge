import pytest
from gistapi.gistapi import app as real_app


@pytest.fixture()
def app():
    real_app.config.update({
        "TESTING": True,
    })

    yield real_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

