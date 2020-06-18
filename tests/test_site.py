'''from textwrap import dedent

import pytest
from flask import Flask

@pytest.fixture(scope='session')
def app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return app.response_class('OK')

    return app
'''

'''import pytest
from flask import g
from flask import session
from learning_flashcards import app


'''Test that viewing a page renders without template errors '''
@pytest.mark.parametrize('page, result',
                         [
                             ("/", 200)
                         ]
                         )
def test_page(client, app, page, result):
    assert client.get(page).status_code == result

'''

from learning_flashcards import create_app

class TestSite:

    def test_app(client):
        assert client.get(url_for('myview')).status_code == 200

