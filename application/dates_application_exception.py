from enum import Enum


class DatesApplicationException(Exception):

    class ErrorType(Enum):
        UNKNOWN = 0
        SYSTEM_ERROR = 1
        BAD_PARAMETERS = 2

    def __init__(self, error_type: ErrorType = ErrorType.UNKNOWN, message: str = ''):
        self.error_type = error_type
        self.message = message
