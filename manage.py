from myapp import create_app, db

from flask_script import Manager, Shell

from flask_migrate import Migrate, MigrateCommand

from myapp.models import User, Category, Recipe

app = create_app('development')

manager = Manager(app)

migrate = Migrate(app, db)

def make_shell_context():
    """Automatically import object instances in the shell context"""
    return dict(app=app, db=db, User=User, Category=Category, Recipe=Recipe)
manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
 