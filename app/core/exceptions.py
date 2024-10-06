from fastapi import HTTPException

class CustomHTTPException(HTTPException):
    """Custom HTTP Exception class."""

    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)
