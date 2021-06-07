from flask import jsonify

userid = 12
category_dict={
    'hat' : ['009', '007'],
    'top' : ['020', '002', '001'],
    'bottom' : ['003', '022'],
    'shoes' : ['018', '005'],
    'bag' : ['004', '054']
}

class WrongRequestForm(Exception):
    def __init__(self, message="요청값이 올바르지 않습니다.", status=400):
        self.message = message
        self.status = status

def error_handler_400(error):
   return jsonify(error='bad request', message='요청값이 올바르지 않습니다. 스웨거를 잘 확인하세요.'), 400


