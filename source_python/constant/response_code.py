from enum import Enum


class ResponseCode(Enum):
    RESPONSE_SUCCESS = 200
    PARAMS_ERROR = 400
    NOT_LOGIN_ERROR = 401
    NO_AUTH_ERROR = 403
    SYSTEM_ERROR = 500
    OPERATION_ERROR = 501
