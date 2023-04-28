import datetime
import logging
from functools import wraps
from pprint import pprint
from flask import request
from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt
import config.config as m_config
from common.result_utils import ResultUtils
from constant.response_code import ResponseCode
from model.user import UserVo
from constant import user_constant

app = Flask(__name__)
CORS(app, resources=r'/*')

app.config['JWT_SECRET_KEY'] = m_config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
jwt = JWTManager(app)
from service.logs_service import insert_logs
from model.logs import LogsAddDto


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return ResultUtils.error(code=ResponseCode.NOT_LOGIN_ERROR.value, data=None,
                             message='token已过期, 请重新登录').to_dict()


@jwt.unauthorized_loader
def my_unauthorized_token_callback(jwt_header):
    return ResultUtils.error(code=ResponseCode.NOT_LOGIN_ERROR.value, data=None, message='请登录').to_dict()


@jwt.invalid_token_loader
def invalid_token(error):
    print(error)
    return ResultUtils.error(code=ResponseCode.NO_AUTH_ERROR.value, data=None,
                             message='token校验失败, 请重新登录').to_dict()


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    try:
        user_vo_temp = jwt_data['sub']
        user_vo = UserVo(id=user_vo_temp['id'], name=user_vo_temp['name'],
                         account=user_vo_temp['account'],
                         role=user_vo_temp['role'], create_time=user_vo_temp['createTime'],
                         update_time=user_vo_temp['updateTime'])
        return user_vo
    except Exception as e:
        logging.error(e)
        return None


def super_admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims['sub']['role'] == user_constant.SUPER_ROLE:
                return fn(*args, **kwargs)
            else:
                return ResultUtils.error(code=ResponseCode.NO_AUTH_ERROR.value, data=None,
                                         message='无权限').to_dict()

        return decorator

    return wrapper


@app.before_request
def before_request():
    if request.url.find('logs') == -1:
        logs_add_dto = LogsAddDto(method=request.method, url=request.url, ip=request.remote_addr)
        insert_logs(logs_add_dto)


from app import user_routes, files_routes, logs_routes, scenic_spots_routes
