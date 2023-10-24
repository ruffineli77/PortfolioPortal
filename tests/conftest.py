
import pytest
from cv_app import create_app
from database import db
from cv_app.config import TestingConfig


@pytest.fixture()
def app():
    app = create_app(config_class=TestingConfig)

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def test_client():
    flask_app = create_app(TestingConfig)
    testing_client = flask_app.test_client()

    with flask_app.app_context():
        db.create_all()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture()
def urls(app):
    url_rules = []
    with app.app_context():
        url_map = app.url_map
        for url_rule in url_map.iter_rules():
            url_rules.append(url_rule)

    yield url_rules


@pytest.fixture()
def client(app):
    return app.test_client()
