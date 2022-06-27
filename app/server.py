from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.controllers.middlewares.logger import LogMiddleware

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///../store.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(server)


from app.models.Item import Item

server.wsgi_app = LogMiddleware(server.wsgi_app)

import app.controllers.routes.index
import app.controllers.routes.catalog