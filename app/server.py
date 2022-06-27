import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.controllers.middlewares.logger import LogMiddleware

server = Flask(__name__)
server.config.from_object(os.getenv('APP_SETTINGS', 'app.config.DevCon'))
db = SQLAlchemy(server)


from app.models.Item import Item

server.wsgi_app = LogMiddleware(server.wsgi_app)

import app.controllers.routes.index
import app.controllers.routes.catalog