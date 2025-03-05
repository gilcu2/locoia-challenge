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

def Given(label: str):
    print(f"Given:\n {label}")


def When(label: str):
    print(f"When:\n {label}")


def Then(label: str):
    print(f"Then:\n {label}")


def And(label: str):
    print(f"And:\n {label}")
