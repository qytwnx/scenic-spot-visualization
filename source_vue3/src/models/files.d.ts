declare namespace FilesModel {

    interface FilesVo {
        id: number;
        name: string;
        type: string;
        size: string;
        url: string;
        uploader: UserModel.UserSimpleVo;
        createTime: string;
        updateTime: string;
    }

    interface FilesQueryDto extends API.PageRequest{
        name: string;
        type: string;
    }
}