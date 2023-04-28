import logging
import os

from model.files import Files, FilesVo, FilesAddDto
from exception.business_exception import BusinessException
from model.page import Page
from mapper.files_mapper import (check_file_name_exists, files_insert, files_page)
from constant.response_code import ResponseCode
from config import config
from mapper.user_mapper import (get_one_user)
from model.user import UserSimpleVo

"""
文件逻辑操作
"""


def upload_files(files, user_id: int) -> str:
    """文件上传"""
    origin_name = files.filename
    file_name = origin_name[:-4]
    file_suffix = origin_name.split('.')[-1]
    files.seek(0)
    file_size = len(files.read())
    files.seek(0)
    flag = check_file_name_exists(name=file_name)
    if flag:
        raise BusinessException(ResponseCode.OPERATION_ERROR.value, "文件已存在，请检查是否已上传或更名重试")
    upload_path = config.UPLOAD_PATH
    file_path = os.path.join(upload_path, origin_name)
    if not os.path.exists(upload_path):
        try:
            os.mkdir(upload_path)
        except Exception as e:
            logging.error(str(e))
            os.makedirs(upload_path)
    file_url = config.SERVER_IP + '/files/download/' + file_name + '.' + file_suffix
    files_add_dto = FilesAddDto(name=file_name, file_type=file_suffix, size=file_size, url=file_url, uploader=user_id)
    result = files_insert(files_add_dto)
    if result:
        files.save(file_path)
    return file_url


def page_files(page_num: int, page_size: int, name: str, files_type: str) -> Page:
    """用户分页"""
    params = ['%' + name.strip() + '%', '%' + files_type.strip() + '%']
    result = files_page(page_num=page_num, page_size=page_size, params=params)
    files_list = result[1]
    files_vo_list = []
    for item in files_list:
        user = get_one_user(item.uploader)
        user_simple_vo = UserSimpleVo(id=user.id, name=user.name, account=user.account)
        files_vo = FilesVo(id=item.id, name=item.name, file_type=item.type, size=item.size, url=item.url,
                           uploader=user_simple_vo.to_dict(), create_time=item.create_time, update_time=item.update_time)
        files_vo_list.append(files_vo.to_dict())
    return Page(total=result[0], records=files_vo_list).to_dict()
