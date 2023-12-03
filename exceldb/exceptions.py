

class ExcelDBBaseException(Exception):
    """Base class for all exceptions raised by ExcelDB"""
    pass

class DatabaseFileNotFoundError(ExcelDBBaseException):
    """Raised when the database file is not found"""
    pass

