import pytest
from learning_flashcards.app import create_app

def test_site(client):
    assert client.get('/').status_code == 200

