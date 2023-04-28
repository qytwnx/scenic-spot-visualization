from model.user import User
from utils.common_util import connect_mysql
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
用户数据库处理
"""


def check_account_exists(account: str) -> bool:
    """ 检查账号是否存在 """
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"select Count(1) from user where account='{account}' limit 1 "
    cursor.execute(sql)
    db.commit()
    data_len = cursor.fetchall()[0][0]
    cursor.close()
    db.close()
    return data_len > 0


def login_user(account: str, password: str):
    """用户登录"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"select id, name, account, password, role, create_time, update_time from user where account='{account}' and password='{password}' limit 1 "
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchone()
    cursor.close()
    db.close()
    if data is None:
        return data
    else:
        user = User(id=data[0], name=data[1], account=data[2], password=data[3], role=data[4],
                    create_time=data[5], update_time=data[6])
        return user


def check_account_repeat(id: int, account: str) -> bool:
    """更新用户信息时检查是否存在该账号"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"select count(1) from user where id!={id} and account='{account}' limit 1 "
    cursor.execute(sql)
    db.commit()
    data_len = cursor.fetchall()[0][0]
    cursor.close()
    db.close()
    return data_len > 0


def get_one_user(id: int):
    """通过ID获取单个用户信息"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"select id, name, account, password, role, create_time, update_time from user where id={id} limit 1 "
    cursor.execute(sql)
    db.commit()
    data = cursor.fetchone()
    cursor.close()
    db.close()
    if data is None:
        return data
    else:
        user = User(id=data[0], name=data[1], account=data[2], password=data[3], role=data[4],
                    create_time=data[5], update_time=data[6])
        return user


def user_insert(user: User) -> bool:
    """添加用户"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"insert into user(name, account, password, role) Values('{user.name}','{user.account}','{user.password}','{user.role}')"
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


def user_delete(id: int) -> bool:
    """删除用户"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"delete from user where id = {id}"
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


def user_update(user: User) -> bool:
    """用户更新"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"update user set name='{user.name}', account='{user.account}' where id={user.id}"
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


def password_change(account: str, password: str):
    """修改密码"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"update user set password = '{password}' where account = '{account}'"
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


def user_page(page_num: int, page_size: int, params: []):
    """用户分页"""
    search_total = (page_num - 1) * page_size
    print(params)
    db = connect_mysql()
    cursor = db.cursor()
    sql1 = "SELECT COUNT(1) FROM user WHERE name LIKE %s AND account LIKE %s"
    cursor.execute(sql1, params)
    db.commit()
    total = cursor.fetchall()[0][0]
    result = []
    if total <= 0 or (page_num - 1) * page_size > total:
        return total, result
    else:
        sql2 = "SELECT id, name, account, password, role, create_time, update_time FROM user WHERE name LIKE %s AND account LIKE %s ORDER BY id DESC LIMIT " + str(
            search_total) + "," + str(page_size)
        cursor.execute(sql2, params)
        db.commit()
        data = cursor.fetchall()
        for data_item in data:
            user = User(id=data_item[0], name=data_item[1], account=data_item[2], password=data_item[3],
                        role=data_item[4], create_time=data_item[5], update_time=data_item[6])
            result.append(user)
        return total, result
