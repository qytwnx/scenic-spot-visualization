from model.logs import LogsAddDto, Logs
from utils.common_util import connect_mysql
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
日志数据库处理
"""


def logs_insert(logs: LogsAddDto) -> bool:
    """添加日志"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"insert into operation_log(method, url, ip) Values('{logs.method}','{logs.url}','{logs.ip}')"
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


def logs_delete(id: int) -> bool:
    """删除日志"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"delete from operation_log where id = {id}"
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


def logs_delete_batch(ids: []) -> bool:
    """批量删除日志"""
    id_list = [(id,) for id in ids]
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"delete from operation_log where id = %s"
    try:
        cursor.executemany(sql, id_list)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def logs_delete_all() -> bool:
    """删除所有日志"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = "delete from operation_log"
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


def logs_page(page_num: int, page_size: int, params: []):
    """日志分页"""
    search_total = (page_num - 1) * page_size
    print(params)
    db = connect_mysql()
    cursor = db.cursor()
    sql1 = "SELECT COUNT(1) FROM operation_log WHERE method LIKE %s"
    cursor.execute(sql1, params)
    db.commit()
    total = cursor.fetchall()[0][0]
    result = []
    if total <= 0 or (page_num - 1) * page_size > total:
        return total, result
    else:
        sql2 = "SELECT id, method, url, ip, operation_time FROM operation_log WHERE method LIKE %s ORDER BY id DESC LIMIT " + str(
            search_total) + "," + str(page_size)
        cursor.execute(sql2, params)
        db.commit()
        data = cursor.fetchall()
        for data_item in data:
            logs = Logs(id=data_item[0], method=data_item[1], url=data_item[2], ip=data_item[3],
                        operation_time=data_item[4])
            result.append(logs)
        return total, result
