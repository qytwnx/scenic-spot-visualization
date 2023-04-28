from app import app
from common.result_utils import ResultUtils
from constant.response_code import ResponseCode


class BusinessException(Exception):
    pass


@app.errorhandler(BusinessException)
def server_exception(error):
    if len(error.args) == 2:
        return ResultUtils.error(code=error.args[0], data=None, message=str(error.args[1])).to_dict()
    else:
        return ResultUtils.error(code=ResponseCode.OPERATION_ERROR.value, data=None, message=str(error)).to_dict()