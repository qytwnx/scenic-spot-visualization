import request from '@/utils/request'

export default () => {
    const filePage = async (data: FilesModel.FilesQueryDto) => {
        return await request<API.ApiPage<FilesModel.FilesVo>, API.IResponse<API.ApiPage<FilesModel.FilesVo>>>({
            url: `/files/page`,
            method: 'GET',
            params: data
        })
    }
    return { filePage }
}