from typing import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient

from gistapi.app import app as real_app


@pytest.fixture()
def app() -> Generator[Flask, None, None]:
    real_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield real_app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()
