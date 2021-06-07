import os
from datetime import timedelta

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = os.getenv('sherlockodds_db_connection_url')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'Thisissherlockodds'
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = 'super-duper-secret'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
JWT_TOKEN_LOCATION = ["cookies", "headers"]

SQLALCHEMY_POOL_SIZE=32
