import request from '@/utils/request'

export default () => {

    const logsDelete = async (data: number) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/logs/delete/${data}`,
            method: 'DELETE'
        })
    }

    const logsDeleteBatch = async (data: CommonModel.DeleteBatchDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/logs/delete/batch`,
            method: 'POST',
            data: data
        })
    }

    const logsDeleteAll = async () => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/logs/delete/all`,
            method: 'DELETE'
        })
    }


    const logsPage = async (data: LogsModel.LogsQueryDto) => {
        return await request<API.ApiPage<LogsModel.LogsVo>, API.IResponse<API.ApiPage<LogsModel.LogsVo>>>({
            url: `/logs/page`,
            method: 'GET',
            params: data
        })
    }
    return { logsDelete, logsDeleteBatch, logsDeleteAll, logsPage }
}