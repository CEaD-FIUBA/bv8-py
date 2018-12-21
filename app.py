from flask import flask
from flask_restful import Api,Resource,reqparse

app = Flash(__name__)
api = Api(app)

class Caption(Resource):
    def get(self,id):
        return 'Hello',200

api.add_resource(Caption,"captions/<string:id>")

app.run(debug=True)
