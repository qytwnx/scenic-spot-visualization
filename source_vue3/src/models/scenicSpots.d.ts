declare namespace ScenicSpotsModel {
    interface ScenicSpotsAddDto {
        name: string;
        level: string;
        province: string;
        city: string;
        address: string;
        introduction: string;
        heat: string;
        price: string;
        sales: string;
        image: string;
        info: string;
        comment: string;
    }

    interface ScenicSpotsUpdateDto {
        id: number;
        name: string;
        level: string;
        province: string;
        city: string;
        address: string;
        introduction: string;
        heat: string;
        price: string;
        sales: string;
        image: string;
        info: string;
        comment: string;
    }

    interface ScenicSpotsVo {
        id: number;
        name: string;
        level: string;
        province: string;
        city: string;
        address: string;
        introduction: string;
        heat: string;
        price: string;
        sales: string;
        image: string;
        info: string;
        comment: string;
        createTime: string;
        updateTime: string;
    }


    interface ScenicSpotsQueryDto extends API.PageRequest {
        name: string;
    }
}