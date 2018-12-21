from flask import Flask
from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)

class Caption(Resource):
    def get(self,id):
        return 'Download caption by {}'.format(id),200

class Check(Resource):
    def get(self):
        return 'OK',200

api.add_resource(Caption,"/captions/<string:id>")
api.add_resource(Check,"/")


app.run(debug=True)
