import logging

from constant.response_code import ResponseCode
from exception.business_exception import BusinessException
from model.logs import LogsAddDto, LogsVo
from mapper.logs_mapper import logs_insert, logs_delete, logs_delete_batch, logs_delete_all, logs_page
from model.page import Page

"""
日志逻辑处理
"""


def insert_logs(logs: LogsAddDto):
    """日志添加"""
    logs_insert(logs)


def delete_logs(id: int):
    """日志删除"""
    if id == 0:
        logging.error("参数错误，未收到ID")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到ID")
    print(id)
    result = logs_delete(id=id)
    return result


def delete_logs_batch(ids: []):
    """日志批量删除"""
    if len(ids) == 0:
        logging.error("参数错误，未收到ID")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到ID")
    result = logs_delete_batch(ids)
    return result


def delete_logs_all():
    """删除所有日志"""
    result = logs_delete_all()
    return result


def page_logs(page_num: int, page_size: int, method: str):
    """日志分页"""
    params = ['%' + method.strip() + '%']
    result = logs_page(page_num=page_num, page_size=page_size, params=params)
    logs_list = result[1]
    logs_vo_list = []
    for item in logs_list:
        logs_vo = LogsVo(id=item.id, method=item.method, url=item.url, ip=item.ip, operation_time=item.operation_time)
        logs_vo_list.append(logs_vo.to_dict())
    return Page(total=result[0], records=logs_vo_list).to_dict()
