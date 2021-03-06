from app import create_app
import pytest
import config
from sqlalchemy import create_engine, text
import json
from app import app
from flask_jwt_extended import create_access_token

database = create_engine(config.test_config['DB_URL'], encoding ='utf=8', max_overflow=0)

@pytest.fixture
def api():
    app = create_app()
    app.config.from_pyfile("config.py")
    app.config['TEST']=True
    api= app.test_client()

    return api

def test_get_access_token_refresh(api):
    new_user= {"email": "magic@gmail.com",
    "name": "magic",
    "provider": "KAKAO",
    "uid": "234324"}
    resp = api.post(
        '/auth/access-token',
        data = json.dumps(new_user),
        content_type ='application/json'
    )
    assert resp.status_code ==200

    resp_json = json.loads(resp.data.decode('utf-8'))
    new_user_access_token = resp_json['access_token']
    new_user_refresh_token = resp_json['refresh_token']

    resp = api.post(
        'auth/hello',
        headers = {'Authorization': "Bearer " +new_user_refresh_token}
    )
    assert resp.status_code ==200


def test_validation(api):
    new_user= {"email": "magic@gmail.com",
    "name": "magic",
    "provider": "asd",
    "uid": "234324"}
    resp = api.post(
        '/auth/access-token',
        data = json.dumps(new_user),
        content_type ='application/json'
    )
    with pytest.raises(Exception) as execinfo:
        raise Exception('provider이상')
    assert resp.status_code ==422
    assert execinfo.value.args[0]=='provider이상'


def test_unauthorized(api):
    # 401 어세스 토큰 없으면 401 리턴하는지 확인
    resp = api.get(
        'mypage/my-looks',
    )
    assert resp.status_code ==401

    resp = api.get(
        'mypage/my-looks/3',
    )
    assert resp.status_code ==401

    resp = api.post(
        'mypage/my-looks/info',
    )
    assert resp.status_code ==401

    resp = api.get(
        'looks/items',
    )
    assert resp.status_code ==401

    resp = api.get(
        'tinder/look',
    )
    assert resp.status_code == 401

    resp = api.post(
        'tinder/confirm',
    )
    assert resp.status_code == 401

    resp = api.put(
        'tinder/thumbs/6',
    )
    assert resp.status_code == 401

def test_get_mylooks():

    identity =10
    with app.test_client() as client:
        with app.app_context():

            access_token = create_access_token(identity=identity,fresh=True)
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            response = client.get('/mypage/my-looks', headers=headers)
            assert response.status_code == 200

def test_mylook_detail():

    identity =10
    with app.test_client() as client:
        with app.app_context():

            access_token = create_access_token(identity=identity,fresh=True)
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            response = client.get('/mypage/my-looks/3', headers=headers)
            assert response.status_code == 200

def test_mylook_detail():
    ids = {
    "hat_id" : "123",
    "top_id" : "234",
    "bottom_id" : "345",
    "shoes_id" : "456",
    "bag_id": "678"
    }
    identity =10
    with app.test_client() as client:
        with app.app_context():

            access_token = create_access_token(identity=identity,fresh=True)
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            response = client.post('/mypage/my-looks/info', data = json.dumps(ids), headers=headers)
            assert response.status_code == 200



def test_get_thumbs():
    new_thumb={
        'id' : '4',
    'userid':"10",
        "lookid":"10",
        "created":"2021-03-02"
    }

    database.execute(text("""
          INSERT INTO Thumb (
              id,
              userid,
              lookid,
              created
          ) VALUES (
              :id,
              :userid,
              :lookid,
              :created
          )
      """), new_thumb)
    identity =10
    with app.test_client() as client:
        with app.app_context():

            access_token = create_access_token(identity=identity,fresh=True)
            headers = {
                'Authorization': 'Bearer {}'.format(access_token)
            }
            response = client.get('/mypage/thumbs?lookid=10', headers=headers)
            assert response.status_code == 200