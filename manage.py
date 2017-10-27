from myapp import create_app, db

from flask_script import Manager, Shell

app = create_app('default')

manager = Manager(app)

def make_shell_context():
    """Creates the custom context for the python shell"""
    return dict(app=app)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
 