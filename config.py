import os
from datetime import timedelta

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://suram:suram@elice-kdt-ai-track-vm-distribute-12.koreacentral.cloudapp.azure.com:3306/muindo?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'Thisissherlockodds'
PROPAGATE_EXCEPTIONS = True
JWT_SECRET_KEY = 'super-duper-secret'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

SQLALCHEMY_POOL_SIZE=32

test_db ={
    'user' :'test',
    'password':'password',
    'host' : 'localhost',
    'port' : 3306,
    'database' : 'test_db'
}

test_config = {
    'DB_URL': f"mysql+pymysql://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8"
}