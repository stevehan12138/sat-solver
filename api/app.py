from flask import Flask
from flask_restful import Api
from config import Config
from resources import WritingResource, ReadingResource, MathResource

def register_extensions(app):
    pass

def create_app():
    app = Flask("aE5tSQPC51AFDUzOE3U3t5Ddz")
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app

def register_resources(app):
    api = Api(app)
    api.add_resource(WritingResource, "/api/writing")
    api.add_resource(ReadingResource, "/api/reading")
    api.add_resource(MathResource, "/api/math")

if __name__ == '__main__':
    app = create_app()
    app.run()
