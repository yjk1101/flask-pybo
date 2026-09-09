from flask import Blueprint

# Blueprint: 라우팅 함수를 체계적으로 관리
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello Pybo!'

@bp.route('/hello')
def hello():
    return 'Hello page!'