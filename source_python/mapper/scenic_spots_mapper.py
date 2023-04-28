from model.scenic_spots import ScenicSpotsAddDto, ScenicSpots, ScenicSpotsUpdateDto
from utils.common_util import connect_mysql
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode
from model.common import CountVo, SalesVo

"""
景点数据库处理
"""


def scenic_spots_insert(scenic_spots_add_dto: ScenicSpotsAddDto) -> bool:
    """添加景点"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"insert into scenic_spots(name, level, province, city, address, introduction, heat, price, sales, image, info, comment) Values('{scenic_spots_add_dto.name}','{scenic_spots_add_dto.level}','{scenic_spots_add_dto.province}','{scenic_spots_add_dto.city}','{scenic_spots_add_dto.address}','{scenic_spots_add_dto.introduction}','{scenic_spots_add_dto.heat}','{scenic_spots_add_dto.price}','{scenic_spots_add_dto.sales}','{scenic_spots_add_dto.image}','{scenic_spots_add_dto.info}','{scenic_spots_add_dto.comment}')"
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


def scenic_spots_delete(id: int) -> bool:
    """删除景点"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"delete from scenic_spots where id = {id}"
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


def scenic_spots_delete_batch(ids: []) -> bool:
    """批量删除景点"""
    id_list = [(id,) for id in ids]
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"delete from scenic_spots where id = %s"
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


def scenic_spots_update(data: ScenicSpotsUpdateDto) -> bool:
    """景点更新"""
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"update scenic_spots set name='{data.name}', level='{data.level}', province='{data.province}', city='{data.city}', address='{data.address}', introduction='{data.introduction}', heat='{data.heat}', price='{data.price}', sales='{data.sales}', image='{data.image}', info='{data.info}', comment='{data.comment}'  where id={data.id}"
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


def scenic_spots_page(page_num: int, page_size: int, params: []):
    """景点分页"""
    search_total = (page_num - 1) * page_size
    db = connect_mysql()
    cursor = db.cursor()
    sql1 = "SELECT COUNT(1) FROM scenic_spots WHERE name LIKE %s"
    cursor.execute(sql1, params)
    db.commit()
    total = cursor.fetchall()[0][0]
    result = []
    if total <= 0 or (page_num - 1) * page_size > total:
        return total, result
    else:
        sql2 = "SELECT id, name, level, province, city, address, introduction, heat, price, sales, image, info, comment, create_time, update_time FROM scenic_spots WHERE name LIKE %s ORDER BY id DESC LIMIT " + str(
            search_total) + "," + str(page_size)
        cursor.execute(sql2, params)
        db.commit()
        data = cursor.fetchall()
        for data_item in data:
            scenic_spots = ScenicSpots(id=data_item[0], name=data_item[1], level=data_item[2], province=data_item[3],
                                       city=data_item[4], address=data_item[5], introduction=data_item[6],
                                       heat=data_item[7],
                                       price=data_item[8], sales=data_item[9], image=data_item[10], info=data_item[11],
                                       comment=data_item[12], create_time=data_item[13], update_time=data_item[14])
            result.append(scenic_spots)
        return total, result


def get_count_by_province(data: str) -> CountVo:
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT COUNT(*) FROM scenic_spots WHERE province = '{data}'"
    try:
        cursor.execute(sql)
        db.commit()
        total = cursor.fetchall()[0][0]
        return CountVo(name=data, value=total)
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_count_by_level(data: str) -> CountVo:
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT COUNT(*) FROM scenic_spots WHERE level = '{data}'"
    try:
        cursor.execute(sql)
        db.commit()
        total = cursor.fetchall()[0][0]
        return CountVo(name=data, value=total)
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_top50_by_heat() -> list[CountVo]:
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT name, heat FROM scenic_spots WHERE id%3=0 ORDER BY heat DESC LIMIT 40,30"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        result = []
        for data_item in data:
            print(data_item)
            count = CountVo(name=data_item[0], value=float(data_item[1]) * 100)
            result.append(count.to_dict())
        return result
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_index_recommend_scenic_spots():
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT id, name, level, province, city, address, introduction, heat, price, sales, image, info, comment, create_time, update_time FROM scenic_spots ORDER BY heat DESC, sales DESC, price ASC LIMIT 10"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        result = []
        for data_item in data:
            f_data = ScenicSpots(id=data_item[0], name=data_item[1], level=data_item[2], province=data_item[3],
                                 city=data_item[4], address=data_item[5], introduction=data_item[6],
                                 heat=data_item[7],
                                 price=data_item[8], sales=data_item[9], image=data_item[10], info=data_item[11],
                                 comment=data_item[12], create_time=data_item[13], update_time=data_item[14])
            result.append(f_data.to_dict())
        return result
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def scenic_spots_index_info():
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT name, info FROM scenic_spots ORDER BY heat DESC, sales DESC, price LIMIT 30"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        result = []
        for data_item in data:
            f_data = CountVo(name=data_item[0], value=data_item[1])
            result.append(f_data.to_dict())
        return result
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def scenic_spots_index_comment():
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT name, comment FROM scenic_spots WHERE comment NOT IN ('暂未评价', '用户未点评，系统默认好评。') ORDER BY heat DESC, sales DESC, price LIMIT 30"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        result = []
        for data_item in data:
            f_data = CountVo(name=data_item[0], value=data_item[1])
            result.append(f_data.to_dict())
        return result
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_count_by_province_city(province: str, city: str) -> CountVo:
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT COUNT(*) FROM scenic_spots WHERE province = '{province}' AND city = '{city}'"
    try:
        cursor.execute(sql)
        db.commit()
        total = cursor.fetchall()[0][0]
        return CountVo(name=city, value=total)
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_province_count_by_level(province: str, level: str) -> CountVo:
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT COUNT(*) FROM scenic_spots WHERE level = '{level}' AND province = '{province}'"
    try:
        cursor.execute(sql)
        db.commit()
        total = cursor.fetchall()[0][0]
        return CountVo(name=level, value=total)
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def scenic_spots_province_comment(name: str):
    db = connect_mysql()
    cursor = db.cursor()
    print(name)
    sql = f"SELECT name, comment FROM scenic_spots WHERE comment NOT IN ('暂未评价', '用户未点评，系统默认好评。') AND province = '{name}' ORDER BY heat DESC, sales DESC, price LIMIT 50"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        result = []
        for data_item in data:
            f_data = CountVo(name=data_item[0], value=data_item[1])
            result.append(f_data.to_dict())
        return result
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def scenic_spots_province_sales(province: str):
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT name, sales FROM scenic_spots WHERE province = '{province}' ORDER BY heat DESC, sales DESC, price"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        x = []
        y = []
        for data_item in data:
            x.append(data_item[0])
            y.append(data_item[1])
        sales_vo = SalesVo(x=x, y=y)
        return sales_vo
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()


def get_on_by_all_rank(province: str, city: str):
    db = connect_mysql()
    cursor = db.cursor()
    sql = f"SELECT id, name, level, province, city, address, introduction, heat, price, sales, image, info, comment, create_time, update_time FROM scenic_spots WHERE province = '{province}' AND city = '{city}' ORDER BY heat DESC, sales DESC, price LIMIT 1"
    try:
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchone()

        f_data = ScenicSpots(id=data[0], name=data[1], level=data[2], province=data[3], city=data[4], address=data[5],
                             introduction=data[6], heat=data[7], price=data[8], sales=data[9], image=data[10],
                             info=data[11], comment=data[12], create_time=data[13], update_time=data[14])
        return f_data
    except Exception as e:
        db.rollback()
        raise BusinessException(ResponseCode.SYSTEM_ERROR.value, str(e))
    finally:
        cursor.close()
        db.close()
