from flask import Flask
from flask_restful import Api,Resource,reqparse
import os
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

print(os.environ['PORT'])
app.run(debug=True,port=os.environ['PORT'])
