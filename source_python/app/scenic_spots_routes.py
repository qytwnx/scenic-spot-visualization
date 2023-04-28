import logging

from flask import request
from flask_jwt_extended import jwt_required

from app import app, super_admin_required
from model.scenic_spots import ScenicSpotsAddDto, ScenicSpotsUpdateDto
from common.result_utils import ResultUtils
from service.scenic_spots_service import (insert_scenic_spots, delete_scenic_spots, delete_scenic_spots_batch,
                                          page_scenic_spots, update_scenic_spots, index_count_ranking_scenic_spots,
                                          index_heat_top50_scenic_spots, index_level_scenic_spots,
                                          index_recommend_scenic_spots, index_info_scenic_spots,
                                          index_comment_scenic_spots, province_count_ranking_scenic_spots,
                                          province_level_scenic_spots, province_comment_scenic_spots,
                                          province_sales_scenic_spots)
from exception.business_exception import BusinessException
from constant.response_code import ResponseCode

"""
景点操作路由
"""


@app.route('/scenic-spots/add', methods=['POST'])
@jwt_required()
def scenic_spots_add():
    """添加景点"""
    try:
        request_data = request.json
        add_dto = ScenicSpotsAddDto(name=request_data['name'], level=request_data['level'],
                                    province=request_data['province'], city=request_data['city'],
                                    address=request_data['address'], introduction=request_data['introduction'],
                                    heat=request_data['heat'], price=request_data['price'], sales=request_data['sales'],
                                    image=request_data['image'], info=request_data['info'],
                                    comment=request_data['comment'])
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = insert_scenic_spots(data=add_dto)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def scenic_spots_delete(id):
    result = delete_scenic_spots(id=id)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/delete/batch', methods=['POST'])
@jwt_required()
def scenic_spots_delete_batch():
    """批量删除景点"""
    try:
        request_data = request.json
        ids = request_data['ids']
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = delete_scenic_spots_batch(ids=ids)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/update', methods=['POST'])
@jwt_required()
def scenic_spots_update():
    """更新景点"""
    try:
        request_data = request.json
        update_dto = ScenicSpotsUpdateDto(id=request_data['id'], name=request_data['name'], level=request_data['level'],
                                          province=request_data['province'], city=request_data['city'],
                                          address=request_data['address'], introduction=request_data['introduction'],
                                          heat=request_data['heat'], price=request_data['price'],
                                          sales=request_data['sales'],
                                          image=request_data['image'], info=request_data['info'],
                                          comment=request_data['comment'])
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = update_scenic_spots(data=update_dto)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/page', methods=['GET'])
@jwt_required()
def scenic_spots_page():
    """景点分页"""
    try:
        page_num = request.args.get("pageNum")
        page_size = request.args.get("pageSize")
        name = request.args.get("name")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = page_scenic_spots(page_num=int(page_num), page_size=int(page_size), name=name)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/count/ranking', methods=['GET'])
def scenic_spots_index_count_ranking():
    """首页各省排名"""
    result = index_count_ranking_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/heat/top', methods=['GET'])
def scenic_spots_index_heat_top50():
    """首页热度排名前五十"""
    result = index_heat_top50_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/level', methods=['GET'])
def scenic_spots_index_level():
    """首页等级分布"""
    result = index_level_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/recommend', methods=['GET'])
def scenic_spots_index_recommend():
    """首页等级分布"""
    result = index_recommend_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/info', methods=['GET'])
def scenic_spots_index_info():
    """首页等级分布"""
    result = index_info_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/index/comment', methods=['GET'])
def scenic_spots_index_comment():
    """首页等级分布"""
    result = index_comment_scenic_spots()
    return ResultUtils.success(data=result).to_dict()


# 二级页面
@app.route('/scenic-spots/province/count/ranking', methods=['GET'])
def scenic_spots_province_count_ranking():
    """首页各省排名"""
    try:
        name = request.args.get("name")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = province_count_ranking_scenic_spots(name)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/province/level', methods=['GET'])
def scenic_spots_province_level():
    """首页等级分布"""
    try:
        name = request.args.get("name")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = province_level_scenic_spots(name=name)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/province/comment', methods=['GET'])
def scenic_spots_province_comment():
    """首页等级分布"""
    try:
        name = request.args.get("name")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = province_comment_scenic_spots(name=name)
    return ResultUtils.success(data=result).to_dict()


@app.route('/scenic-spots/province/sales', methods=['GET'])
def scenic_spots_province_sales():
    """首页等级分布"""
    try:
        name = request.args.get("name")
    except Exception as e:
        logging.error(e)
        raise BusinessException(ResponseCode.PARAMS_ERROR.value, '参数不足')
    result = province_sales_scenic_spots(name=name)
    return ResultUtils.success(data=result.to_dict()).to_dict()
