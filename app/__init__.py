from flask import Flask
from flask import Blueprint
from flask_restful import Api, Resource 


import os

#local import
from views import MyIncidents, MyIncident


def create_app(config_name=os.getenv('APP-SETTINGS')):
    app = Flask(__name__)
    app.register_blueprint(v1)
    return app 

v1 = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api = Api(v1)


## setup API resource routing
api.add_resource(MyIncidents, '/incidents', endpoint='incidents')
api.add_resource(MyIncident, '/incidents/<int:id>', endpoint='incident')