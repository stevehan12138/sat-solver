from flask_restful import Resource
from flask import request
from http import HTTPStatus
from ml import DummyModel

class ReadingResource(Resource):

    def post(self):
        data = request.get_json()

        try:
            data["m1"]
            data["m2"]
            data["m3"]
            data["m4"]
            data["passage"]
            data["query"]
        except KeyError:
            return "Not all keys are present", HTTPStatus.BAD_REQUEST

        res = DummyModel.predict(data)
        return res, HTTPStatus.OK

class WritingResource(Resource):

    def post(self):
        data = request.get_json()

        try:
            data["m1"]
            data["m2"]
            data["m3"]
            data["m4"]
            data["query"]
        except KeyError:
            return "Not all keys are present", HTTPStatus.BAD_REQUEST

        res = DummyModel.predict(data)
        return res, HTTPStatus.OK

class MathResource(Resource):

    def post(self):
        data = request.get_json()

        try:
            data["m1"]
            data["m2"]
            data["m3"]
            data["m4"]
            data["query"]
        except KeyError:
            return "Not all keys are present", HTTPStatus.BAD_REQUEST

        res = DummyModel.predict(data)
        return res, HTTPStatus.OK
