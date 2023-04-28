import logging
from model.user import UserAddDto, User, UserUpdateDto, UserVo, UserLoginDto, UserChangePasswordDto
from utils.common_util import get_md5
from exception.business_exception import BusinessException
from model.page import Page
from mapper.user_mapper import (user_page, user_insert, check_account_exists, user_delete, get_one_user,
                                check_account_repeat, user_update, password_change, login_user)
from constant import user_constant
from constant.response_code import ResponseCode

"""
用户逻辑操作
"""


def user_login(user_login_dto: UserLoginDto) -> UserVo:
    """用户登录"""
    if len(user_login_dto.password) < 8 or len(user_login_dto.password) > 16:
        logging.error("密码长度为8-16字符")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "密码长度为8-16字符")
    flag = check_account_exists(user_login_dto.account)
    if not flag:
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "手机号不存在")
    password = get_md5(user_login_dto.password)
    result = login_user(account=user_login_dto.account, password=password)
    if result is None:
        logging.error("手机号或密码错误")
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "手机号或密码错误")
    user_vo = UserVo(id=result.id, name=result.name, account=result.account,
                     role=result.role, create_time=result.create_time, update_time=result.update_time)
    return user_vo


def insert_user(user_add_dto: UserAddDto) -> bool:
    """添加用户"""
    if len(user_add_dto.name) == 0 or len(user_add_dto.account) == 0 or len(user_add_dto.password) == 0:
        logging.error("请求参数不完整")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "请求参数不完整")
    if len(user_add_dto.account) != 11:
        logging.error("手机号长度不正确")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "手机号长度不正确")
    if len(user_add_dto.password) < 8 or len(user_add_dto.password) > 16:
        logging.error("密码长度为8-16字符")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "密码长度为8-16字符")

    flag = check_account_exists(user_add_dto.account)
    if flag:
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "邮箱已存在")
    encrypt_password = get_md5(user_add_dto.password)
    user = User(id=None, name=user_add_dto.name, account=user_add_dto.account,
                password=encrypt_password, role=user_add_dto.role)
    result = user_insert(user)
    return result


def delete_user(id: int) -> bool:
    """删除用户"""
    if id == 0:
        logging.error("参数错误，未收到ID")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到ID")
    print(id)
    result = user_delete(id=id)
    return result


def update_user(user_update_dto: UserUpdateDto) -> bool:
    """更新用户"""
    if len(user_update_dto.name) == 0 or len(user_update_dto.account) == 0:
        logging.error("请求参数不完整")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "请求参数不完整")
    if len(user_update_dto.account) != 11:
        logging.error("手机号长度不正确")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "手机号长度不正确")
    old_result = get_one_user(user_update_dto.id)
    if old_result is None:
        logging.error("账号信息有误，请重试")
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "账号信息有误，请重试")
    print(old_result)
    if user_update_dto.name == old_result.name and user_update_dto.account == old_result.account:
        logging.info("信息无变动，无需修改")
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "信息无变动，无需修改")
    if check_account_repeat(user_update_dto.id, user_update_dto.account):
        logging.error("手机号已存在")
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "手机号已存在")
    user = User(id=user_update_dto.id, name=user_update_dto.name, account=user_update_dto.account,
                password=None, role=None, create_time=None,
                update_time=None)
    result = user_update(user)
    return result


def change_password(change_password_dto: UserChangePasswordDto) -> bool:
    if change_password_dto.id is None or len(change_password_dto.account) == 0 or len(
            change_password_dto.old_password) == 0 or len(change_password_dto.password) == 0 or \
            len(change_password_dto.re_password) == 0:
        logging.error("请求参数不完整")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "请求参数不完整")
    result = login_user(account=change_password_dto.account, password=get_md5(change_password_dto.old_password))
    if change_password_dto.password != change_password_dto.re_password:
        logging.error("两次输入密码不一致")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "两次输入密码不一致")
    if result is None:
        logging.error("旧密码错误")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "旧密码错误")
    result = password_change(account=change_password_dto.account,
                             password=get_md5(password=change_password_dto.password))
    return result


def reset_password(account: str) -> bool:
    """重置密码"""
    if len(account) == 0:
        logging.error("参数错误，未收到手机号")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到手机号")
    flag = check_account_exists(account)
    if not flag:
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "手机号不存在")
    password = get_md5(user_constant.DEFAULT_PASSWORD)
    result = password_change(account=account, password=password)
    return result


def page_user(page_num: int, page_size: int, name: str, account: str) -> Page:
    """用户分页"""
    params = ['%' + name.strip() + '%', '%' + account.strip() + '%']
    result = user_page(page_num=page_num, page_size=page_size, params=params)
    user_list = result[1]
    user_vo_list = []
    for item in user_list:
        user_vo = UserVo(id=item.id, name=item.name, account=item.account, role=item.role,
                         create_time=item.create_time, update_time=item.update_time)
        user_vo_list.append(user_vo.to_dict())

    return Page(total=result[0], records=user_vo_list).to_dict()
