from rimbot.webserver.server import server
from rimbot.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

server.config.from_object(Config)
database = SQLAlchemy(server)
migrate = Migrate(server, database)
bootstrap = Bootstrap(server)