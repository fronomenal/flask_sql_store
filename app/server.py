import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.controllers.middlewares.logger import LogMiddleware
from flask_bcrypt import Bcrypt

server = Flask(__name__)
server.config.from_object(os.getenv('APP_SETTINGS', 'app.config.DevCon'))
db = SQLAlchemy(server)
migrate = Migrate(server, db)
bcrypt = Bcrypt(server)

from app.models.Item import Item
from app.models.User import User

server.wsgi_app = LogMiddleware(server.wsgi_app)

import app.controllers.routes.index
import app.controllers.routes.register
import app.controllers.routes.login
import app.controllers.routes.catalog