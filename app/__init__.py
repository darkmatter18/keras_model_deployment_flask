
"""
Setup flask
"""
from flask import Flask
from app.model.model import init

def create_app():
    app = Flask(__name__, static_folder='static')
    init()
    return app

app = create_app()
# app = Flask(__name__, static_folder='static')
"""
Register blueprints for api and quiz
"""
from app.api.routes import api_blueprint
from app.webapp.routes import webapp_blueprint

app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(webapp_blueprint, url_prefix='')