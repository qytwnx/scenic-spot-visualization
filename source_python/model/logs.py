"""日志"""


class LogsAddDto:
    """日志添加实体"""

    def __init__(self, method, url, ip):
        self.method = method
        self.url = url
        self.ip = ip


class Logs:
    """日志实体"""

    def __init__(self, id, method, url, ip, operation_time=None):
        self.id = id
        self.method = method
        self.url = url
        self.ip = ip
        self.operation_time = operation_time

    def to_dict(self):
        return {
            "id": self.id,
            "method": self.method,
            "url": self.url,
            "ip": self.ip,
            "operationTime": self.operation_time
        }


class LogsVo:
    """日志返回模型"""

    def __init__(self, id, method, url, ip, operation_time=None):
        self.id = id
        self.method = method
        self.url = url
        self.ip = ip
        self.operation_time = operation_time

    def to_dict(self):
        return {
            "id": self.id,
            "method": self.method,
            "url": self.url,
            "ip": self.ip,
            "operationTime": self.operation_time.strftime("%Y-%m-%d %H:%M:%S")
        }
