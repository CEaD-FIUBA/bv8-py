from flask import Flask
from flask_restful import Api,Resource,reqparse
from os import environ
from captions import download_caption,get_authenticated_service
import argparse

app = Flask(__name__)
api = Api(app)
args = argparse.Namespace()
args.action = 'download'
args.auth_host_name='http://bbv8-py.herokuapp.com'
args.auth_host_port=[8081, 8090]
args.file=None
args.language='en'
args.logging_level='ERROR'
args.name='YouTube for Developers'
args.noauth_local_webserver=False
args.videoid=None

class Caption(Resource):
    def get(self,id):
        youtube = get_authenticated_service(args)
        return {
            'id':id,
            'captions':download_caption(youtube,id,'srt')
        }

class Check(Resource):
    def get(self):
        return 'OK',200

api.add_resource(Caption,"/captions/<string:id>")
api.add_resource(Check,"/")

PORT = '8081' if environ.get('PORT') is None else environ['PORT']
print(PORT)

app.run(debug=True,port=PORT,host='0.0.0.0')
