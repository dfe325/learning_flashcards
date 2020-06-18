from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from learning_flashcards import app, db

import pytest

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "project/tests"])

if __name__ == '__main__':
    manager.run()

