import logging

from constant.response_code import ResponseCode
from exception.business_exception import BusinessException
from model.scenic_spots import ScenicSpots, ScenicSpotsAddDto, ScenicSpotsVo, ScenicSpotsUpdateDto
from model.common import CountProvinceVo
from mapper.scenic_spots_mapper import (scenic_spots_insert, scenic_spots_delete, scenic_spots_delete_batch,
                                        scenic_spots_page, scenic_spots_update, get_count_by_province,
                                        get_top50_by_heat, get_count_by_level, get_index_recommend_scenic_spots,
                                        scenic_spots_index_info, scenic_spots_index_comment, get_count_by_province_city,
                                        get_province_count_by_level, scenic_spots_province_comment,
                                        scenic_spots_province_sales, get_on_by_all_rank)
from model.page import Page
from constant import province_city

"""
景点逻辑处理
"""


def insert_scenic_spots(data: ScenicSpotsAddDto):
    """景点添加"""
    scenic_spots_insert(data)


def delete_scenic_spots(id: int):
    """景点删除"""
    if id == 0:
        logging.error("参数错误，未收到ID")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到ID")
    print(id)
    result = scenic_spots_delete(id=id)
    return result


def delete_scenic_spots_batch(ids: []):
    """景点批量删除"""
    if len(ids) == 0:
        logging.error("参数错误，未收到ID")
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, "参数错误，未收到ID")
    result = scenic_spots_delete_batch(ids)
    return result


def update_scenic_spots(data: ScenicSpotsUpdateDto) -> bool:
    result = scenic_spots_update(data)
    return result


def page_scenic_spots(page_num: int, page_size: int, name: str):
    """景点分页"""
    params = ['%' + name.strip() + '%']
    result = scenic_spots_page(page_num=page_num, page_size=page_size, params=params)
    scenic_spots_list = result[1]
    scenic_spots_vo_list = []
    for item in scenic_spots_list:
        scenic_spots_vo = ScenicSpotsVo(id=item.id, name=item.name, level=item.level, province=item.province,
                                        city=item.city, address=item.address, introduction=item.introduction,
                                        heat=item.heat, price=item.price, sales=item.sales, info=item.info,
                                        comment=item.comment, image=item.image, create_time=item.create_time,
                                        update_time=item.update_time)
        scenic_spots_vo_list.append(scenic_spots_vo.to_dict())
    return Page(total=result[0], records=scenic_spots_vo_list).to_dict()


def index_count_ranking_scenic_spots():
    """首页各省排名"""
    result = []
    for item in province_city.all_province:
        count = get_count_by_province(item)
        result.append(count.to_dict())
    return result


def index_heat_top50_scenic_spots():
    """首页热度排名前五十"""
    return get_top50_by_heat()


def index_level_scenic_spots():
    """首页水平分布"""
    result = []
    for item in province_city.all_level:
        count = get_count_by_level(item)
        result.append(count.to_dict())
    return result


def index_recommend_scenic_spots():
    """首页推荐"""
    return get_index_recommend_scenic_spots()


def index_info_scenic_spots():
    """首页推荐"""
    return scenic_spots_index_info()


def index_comment_scenic_spots():
    """首页推荐"""
    return scenic_spots_index_comment()


# 详情页
def province_count_ranking_scenic_spots(name: str):
    """首页各省排名"""
    result = []
    for item in province_city.get_city_by_province(name=name):
        count = get_count_by_province_city(province=name, city=item)
        count_province_vo = CountProvinceVo(name=count.name, value=count.value, example=None)
        if count.value > 0:
            data = get_on_by_all_rank(province=name, city=item)
            count_province_vo = CountProvinceVo(name=count.name, value=count.value, example=data.to_dict())
        result.append(count_province_vo.to_dict())
    return result


def province_level_scenic_spots(name: str):
    """首页水平分布"""
    result = []
    for item in province_city.all_level:
        count = get_province_count_by_level(province=name, level=item)
        result.append(count.to_dict())
    return result


def province_comment_scenic_spots(name: str):
    """首页推荐"""
    return scenic_spots_province_comment(name=name)


def province_sales_scenic_spots(name: str):
    """首页推荐"""
    return scenic_spots_province_sales(province=name)
