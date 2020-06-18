import pytest
from learning_flashcards import create_app

@pytest.fixture
def app():
    app = create_app()
    return app