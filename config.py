import os
from datetime import timedelta

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:tnfkadlek1@myfirstdb.cwtu7qrvwhdo.ap-northeast-2.rds.amazonaws.com:3306/muindo?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'Thisissherlockodds'
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = 'super-duper-secret'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES= timedelta(days=30)

SQLALCHEMY_POOL_SIZE=32