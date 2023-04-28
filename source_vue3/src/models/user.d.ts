declare namespace UserModel {
    interface UserAddDto {
        name: string;
        account: string;
        password: string;
    }

    interface UserLoginDto {
        account: string;
        password: string;
    }

    interface UserUpdateDto {
        id: number;
        name: string;
        account: string;
    }

    interface UserChangePasswordDto {
        id: number;
        account: string;
        oldPassword: string;
        password: string;
        rePassword: string;
    }

    interface UserVo {
        id: number;
        name: string;
        account: string;
        role: string;
        createTime: string;
        updateTime: string;
    }

    interface UserLoginVo {
        user: UserVo;
        token: string;
    }

    interface UserSimpleVo {
        id: number;
        name: string;
        account: string;
    }

    interface UserQueryDto extends API.PageRequest{
        name: string;
        account: string;
    }
}