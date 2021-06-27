from flask import Flask
from flask_restful import Resource, Api

def create_app():
    app = Flask(__name__)
    api = Api(app)

    from . import music

    api.add_resource(music.Music, '/music')

    return app
