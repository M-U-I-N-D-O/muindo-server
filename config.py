import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = os.getenv('sherlockodds_db_connection_url')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'Thisissherlockodds'
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = 'super-duper-secret'
