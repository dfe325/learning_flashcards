import pytest
from learning_flashcards.app import create_app

@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app

@pytest.fixture
def db_connect():
    return