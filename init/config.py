import os
from init.env import db_connection_url

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = db_connection_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'Thisissherlockodds'
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = 'super-duper-secret'
