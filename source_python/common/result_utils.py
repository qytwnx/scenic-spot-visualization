from constant.response_code import ResponseCode


class ResultUtils:
    def __init__(self, code, data, message):
        self.code = code
        self.data = data
        self.message = message

    @classmethod
    def success(cls, code=ResponseCode.RESPONSE_SUCCESS.value, data=None, message="ok"):
        return cls(code, data, message)

    @classmethod
    def error(cls, code=ResponseCode.RESPONSE_SUCCESS.value, data=None, message="ok"):
        return cls(code, data, message)

    def to_dict(self):
        return {
            "code": self.code,
            "data": self.data,
            "message": self.message
        }
