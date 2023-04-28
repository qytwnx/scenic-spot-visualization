import request from '@/utils/request'

export default () => {

    const loginUser = async (data: UserModel.UserLoginDto) => {
        return await request<UserModel.UserLoginVo, API.IResponse<UserModel.UserLoginVo>>({
            url: `/user/login`,
            method: 'POST',
            data: data
        })
    }

    const userAdd = async (data: UserModel.UserAddDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/user/add`,
            method: 'POST',
            data: data
        })
    }

    const userDelete = async (id: number) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/user/delete/${id}`,
            method: 'DELETE'
        })
    }


    const userUpdate = async (data: UserModel.UserUpdateDto) => {
        return await request<number, API.IResponse<number>>({
            url: `/user/update`,
            method: 'POST',
            data: data
        })
    }

    const passwordChange = async (data: UserModel.UserChangePasswordDto) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/user/password/change`,
            method: 'POST',
            data: data
        })
    }

    const passwordReset = async (account: string) => {
        return await request<boolean, API.IResponse<boolean>>({
            url: `/user/password/reset/${account}`,
            method: 'GET'
        })
    }

    const userCurrent = async () => {
        return await request<UserModel.UserVo, API.IResponse<UserModel.UserVo>>({
            url: `/user/current`,
            method: 'GET'
        })
    }
    const userPage = async (data: UserModel.UserQueryDto) => {
        return await request<API.ApiPage<UserModel.UserVo>, API.IResponse<API.ApiPage<UserModel.UserVo>>>({
            url: `/user/page`,
            method: 'GET',
            params: data
        })
    }
    return { loginUser, userAdd, userDelete, userUpdate, passwordChange, passwordReset, userCurrent, userPage }
}