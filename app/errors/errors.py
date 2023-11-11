from fastapi import HTTPException, status

from app.errors.messages import ErrorMessage


class InternalServerError(HTTPException):
    def __init__(self, detail: str = ErrorMessage.INTERNAL_SERVER_ERROR):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                         detail=detail)


class DuplicateArxivQuery(HTTPException):
    def __init__(self, detail: str = ErrorMessage.DUPLICATE_ARXIV_QUERY):
        super().__init__(status_code=status.HTTP_409_CONFLICT,
                         detail=detail)
