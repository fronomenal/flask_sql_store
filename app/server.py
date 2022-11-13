import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.controllers.middlewares.logger import LogMiddleware
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin

server = Flask(__name__)
server.config.from_object(os.getenv('APP_SETTINGS', 'app.config.DevCon'))
db = SQLAlchemy(server)
migrate = Migrate(server, db)
bcrypt = Bcrypt(server)
login_manager = LoginManager(server)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from app.models.Item import Item
from app.models.User import User

server.wsgi_app = LogMiddleware(server.wsgi_app)

import app.controllers.routes.index
import app.controllers.routes.register
import app.controllers.routes.login
import app.controllers.routes.logout
import app.controllers.routes.catalog