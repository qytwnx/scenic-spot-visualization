import logging
import os

from flask import request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from app import app
from common.result_utils import ResultUtils
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode
from config import config
from service.files_service import (upload_files, page_files)

"""
文件操作路由
"""


@app.route('/files/upload', methods=['POST'])
@jwt_required()
def file_upload():
    """上传文件"""
    if request.method == 'POST':
        file = request.files['file']
        claims = get_jwt()
        user = claims['sub']
        if user is None:
            raise BusinessException(ResponseCode.NO_AUTH_ERROR.value, '权限不足')
        result = upload_files(file, user['id'])
        return ResultUtils.success(data=result).to_dict()
    else:
        return ResultUtils.error(code=ResponseCode.OPERATION_ERROR.value, data=None, message='接口类型错误').to_dict()


@app.route('/files/download/<string:name>', methods=['GET'])
def file_download(name):
    dir_path = os.path.join(config.UPLOAD_PATH)
    return send_from_directory(dir_path, name, as_attachment=True)


@app.route('/files/page', methods=['GET'])
@jwt_required()
def file_page():
    """文件分页"""
    try:
        page_num = request.args.get("pageNum")
        page_size = request.args.get("pageSize")
        name = request.args.get("name")
        file_type = request.args.get("type")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = page_files(page_num=int(page_num), page_size=int(page_size), name=name, files_type=file_type)
    return ResultUtils.success(data=result).to_dict()
