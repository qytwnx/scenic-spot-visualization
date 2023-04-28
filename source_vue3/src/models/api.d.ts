declare namespace API {
    interface PageRequest {
        pageNum: number;
        pageSize: number;
    }

    interface ApiPage<T> {
        total: number;
        records: T[];
    }

    interface IResponse<T> {
        code: number;
        data: T;
        message: string;
    }
}