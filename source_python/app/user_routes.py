import logging

from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
from constant import user_constant
from app import app, super_admin_required
from common.result_utils import ResultUtils
from model.user import UserAddDto, UserUpdateDto, UserLoginDto, UserChangePasswordDto, UserLoginVo
from service.user_service import (insert_user, delete_user, update_user, reset_password, page_user, user_login,
                                  change_password)
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
用户操作路由
"""


@app.route('/user/login', methods=['POST'])
def login():
    try:
        request_data = request.json
        user_login_dto = UserLoginDto(account=request_data['account'], password=request_data['password'])
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = user_login(user_login_dto)
    access_token = create_access_token(
        identity={'id': result.id, 'name': result.name, 'account': result.account,
                  'role': result.role, 'createTime': result.create_time, 'updateTime': result.update_time})
    user_login_vo = UserLoginVo(user=result.to_dict(), token=access_token)
    return ResultUtils.success(data=user_login_vo.to_dict()).to_dict()


@app.route('/user/add', methods=['POST'])
# @super_admin_required()
def user_add():
    """添加用户"""
    try:
        request_data = request.json
        user_add_dto = UserAddDto(name=request_data['name'], account=request_data['account'],
                                  password=request_data['password'], role=user_constant.DEFAULT_ROLE)
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = insert_user(user_add_dto=user_add_dto)
    return ResultUtils.success(data=result).to_dict()


@app.route('/user/delete/<int:id>', methods=['DELETE'])
@super_admin_required()
def user_delete(id):
    """删除用户"""
    result = delete_user(id=id)
    return ResultUtils.success(data=result).to_dict()


@app.route('/user/update', methods=['POST'])
@jwt_required()
def user_update():
    """更新用户"""
    try:
        request_data = request.json
        user_update_dto = UserUpdateDto(id=request_data['id'], name=request_data['name'],
                                        account=request_data['account'])
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = update_user(user_update_dto=user_update_dto)
    return ResultUtils.success(data=result).to_dict()


@app.route('/user/password/change', methods=['POST'])
@jwt_required()
def password_change():
    """用户修改密码"""
    try:
        request_data = request.json
        change_password_dto = UserChangePasswordDto(id=request_data['id'], account=request_data['account'],
                                                    old_password=request_data['oldPassword'],
                                                    password=request_data['password'],
                                                    re_password=request_data['rePassword'])
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = change_password(change_password_dto=change_password_dto)
    return ResultUtils.success(data=result).to_dict()


@app.route('/user/password/reset/<string:account>', methods=['GET'])
@super_admin_required()
def password_reset(account):
    """重置密码"""
    result = reset_password(account=account)
    return ResultUtils.success(data=result).to_dict()


@app.route('/user/current', methods=['GET'])
@jwt_required()
def user_current():
    """获取当前登录用户"""
    claims = get_jwt()
    user = claims['sub']
    return ResultUtils.success(data=user).to_dict()


@app.route('/user/page', methods=['GET'])
@super_admin_required()
def user_page():
    """用户分页"""
    try:
        page_num = request.args.get("pageNum")
        page_size = request.args.get("pageSize")
        name = request.args.get("name")
        account = request.args.get("account")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = page_user(page_num=int(page_num), page_size=int(page_size), name=name, account=account)
    return ResultUtils.success(data=result).to_dict()
