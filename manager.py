import os
from flask.ext.script import Server, Manager
from flask.ext.migrate import Migrate, MigrateCommand

from app import app, db


# app.config.from_object(os.environ['APP_SETTINGS'])
print os.getenv('PORT')

print os.getenv('IP')
migrate = Migrate(app, db)
manager = Manager(app)

server = Server(host=os.getenv('IP'), port=int(os.getenv('PORT')))
manager.add_command("runserver", server)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    