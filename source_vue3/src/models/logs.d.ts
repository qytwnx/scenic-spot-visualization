declare namespace LogsModel {

    interface LogsVo {
        id: number;
        method: string;
        url: string;
        ip: string;
        operation_time: string;
    }

    interface LogsQueryDto extends API.PageRequest{
        method: string;
    }
}