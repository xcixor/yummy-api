from myapp import create_app, db

from flask_script import Manager, Shell

from myapp.models import User, Recipe, Category

app = create_app('development')

manager = Manager(app)

def make_shell_context():
    """Automatically import object instances in the shell context"""
    return dict(app=app, db=db, User=User, Category=Category, Recipe=Recipe)
manager.add_command("shell", Shell(make_context=make_shell_context))

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
 