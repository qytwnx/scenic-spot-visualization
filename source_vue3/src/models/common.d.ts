declare namespace CommonModel {
    interface IProvince {
        name: string,
        tag: string
    }

    interface DeleteBatchDto {
        ids: number[];
    }

    interface CountVo {
        name: string;
        value: string | number;
    }

    interface CountProvinceVo {
        name: string;
        value: string | number;
        example: ScenicSpotsModel.ScenicSpotsVo;
    }

    interface SalesVo {
        x: string[]
        y: number[]
    }
}