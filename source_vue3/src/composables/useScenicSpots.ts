import request from '@/utils/request'

export default () => {

    const scenicSpotsAdd = async (data: ScenicSpotsModel.ScenicSpotsAddDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/scenic-spots/add`,
            method: 'POST',
            data: data
        })
    }

    const scenicSpotsDelete = async (id: number) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/scenic-spots/delete/${id}`,
            method: 'DELETE'
        })
    }

    const scenicSpotsDeleteBatch = async (data: CommonModel.DeleteBatchDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/scenic-spots/delete/batch`,
            method: 'POST',
            data: data
        })
    }

    const scenicSpotsUpdate = async (data: ScenicSpotsModel.ScenicSpotsUpdateDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/scenic-spots/update`,
            method: 'POST',
            data: data
        })
    }

    const scenicSpotsPage = async (data: ScenicSpotsModel.ScenicSpotsQueryDto) => {
        return await request<API.ApiPage<ScenicSpotsModel.ScenicSpotsVo>, API.IResponse<API.ApiPage<ScenicSpotsModel.ScenicSpotsVo>>>({
            url: `/scenic-spots/page`,
            method: 'GET',
            params: data
        })
    }

    // 获取首页数量排名
    const scenicSpotsIndexCountRanking = async () => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/index/count/ranking`,
            method: 'GET',
        })
    }

    // 获取首页热度前五十排名
    const scenicSpotsIndexHeatTop50 = async () => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/index/heat/top`,
            method: 'GET',
        })
    }

    // 获取首页等级分布
    const scenicSpotsIndexLevel = async () => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/index/level`,
            method: 'GET',
        })
    }

    // 获取首页等级分布
    const scenicSpotsIndexRecommend = async () => {
        return await request<ScenicSpotsModel.ScenicSpotsVo[], API.IResponse<ScenicSpotsModel.ScenicSpotsVo[]>>({
            url: `/scenic-spots/index/recommend`,
            method: 'GET',
        })
    }

    // 获取首页资讯
    const scenicSpotsIndexInfo = async () => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/index/info`,
            method: 'GET',
        })
    }

    // 获取首页评论
    const scenicSpotsIndexComment = async () => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/index/comment`,
            method: 'GET',
        })
    }

    /**
     * 省
     */
        // 获取首页评论
    const scenicSpotsProvinceCountRanking = async (name: string) => {
            return await request<CommonModel.CountProvinceVo[], API.IResponse<CommonModel.CountProvinceVo[]>>({
                url: `/scenic-spots/province/count/ranking`,
                method: 'GET',
                params: {name}
            })
        }
    const scenicSpotsProvinceLevel = async (name: string) => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/province/level`,
            method: 'GET',
            params: {name}
        })
    }

    const scenicSpotsProvinceComment = async (name: string) => {
        return await request<CommonModel.CountVo[], API.IResponse<CommonModel.CountVo[]>>({
            url: `/scenic-spots/province/comment`,
            method: 'GET',
            params: {name}
        })
    }

    const scenicSpotsProvinceSales = async (name: string) => {
        return await request<CommonModel.SalesVo, API.IResponse<CommonModel.SalesVo>>({
            url: `/scenic-spots/province/sales`,
            method: 'GET',
            params: {name}
        })
    }
    return {
        scenicSpotsAdd,
        scenicSpotsDelete,
        scenicSpotsDeleteBatch,
        scenicSpotsUpdate,
        scenicSpotsPage,
        scenicSpotsIndexCountRanking,
        scenicSpotsIndexHeatTop50,
        scenicSpotsIndexLevel,
        scenicSpotsIndexRecommend,
        scenicSpotsIndexInfo,
        scenicSpotsIndexComment,
        scenicSpotsProvinceCountRanking,
        scenicSpotsProvinceLevel,
        scenicSpotsProvinceComment,
        scenicSpotsProvinceSales
    }
}