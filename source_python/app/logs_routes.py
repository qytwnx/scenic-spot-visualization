import logging

from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
from constant import user_constant
from app import app, super_admin_required
from common.result_utils import ResultUtils
from model.user import UserAddDto, UserUpdateDto, UserLoginDto, UserChangePasswordDto, UserLoginVo
from service.logs_service import (delete_logs, delete_logs_batch, delete_logs_all, page_logs)
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
日志操作路由
"""


@app.route('/logs/delete/<int:id>', methods=['DELETE'])
@super_admin_required()
def logs_delete(id):
    result = delete_logs(id=id)
    return ResultUtils.success(data=result).to_dict()


@app.route('/logs/delete/batch', methods=['POST'])
@super_admin_required()
def logs_delete_batch():
    """批量删除日志"""
    try:
        request_data = request.json
        ids = request_data['ids']
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = delete_logs_batch(ids=ids)
    return ResultUtils.success(data=result).to_dict()


@app.route('/logs/delete/all', methods=['DELETE'])
@super_admin_required()
def logs_delete_all():
    """删除所有日志"""
    result = delete_logs_all()
    return ResultUtils.success(data=result).to_dict()


@app.route('/logs/page', methods=['GET'])
@super_admin_required()
def logs_page():
    """日志分页"""
    try:
        page_num = request.args.get("pageNum")
        page_size = request.args.get("pageSize")
        method = request.args.get("method")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = page_logs(page_num=int(page_num), page_size=int(page_size), method=method)
    return ResultUtils.success(data=result).to_dict()
