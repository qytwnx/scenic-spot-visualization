from model.files import Files, FilesAddDto
from utils.common_util import connect_mysql
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
文件数据库处理
"""


def check_file_name_exists(name: str) -> bool:
    """检查文件名是否存在"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"select Count(1) from files where name='{name}' limit 1 "
    cursor.execute(sql)
    db.commit()
    data_len = cursor.fetchall()[0][0]
    cursor.close()
    db.close()
    return data_len > 0


def files_insert(files: FilesAddDto) -> bool:
    """添加文件"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"insert into files(name, type, size, url, uploader) Values('{files.name}','{files.type}','{files.size}','{files.url}','{files.uploader}')"
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def files_page(page_num: int, page_size: int, params: []):
    """文件分页"""
    search_total = (page_num - 1) * page_size
    print(params)
    db = connect_mysql()
    cursor = db.cursor()
    sql1 = "SELECT COUNT(1) FROM files WHERE name LIKE %s AND type LIKE %s"
    cursor.execute(sql1, params)
    db.commit()
    total = cursor.fetchall()[0][0]
    result = []
    if total <= 0 or (page_num - 1) * page_size > total:
        return total, result
    else:
        sql2 = "SELECT id, name, type, size, url, uploader, create_time, update_time FROM files WHERE name LIKE %s AND type LIKE %s ORDER BY id DESC LIMIT " + str(
            search_total) + "," + str(page_size)
        cursor.execute(sql2, params)
        db.commit()
        data = cursor.fetchall()
        for data_item in data:
            files = Files(id=data_item[0], name=data_item[1], file_type=data_item[2], size=data_item[3],
                          url=data_item[4], uploader=data_item[5], create_time=data_item[6], update_time=data_item[7])
            result.append(files)
        return total, result
