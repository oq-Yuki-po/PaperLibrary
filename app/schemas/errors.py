from fastapi import status
from pydantic import BaseModel, Field

from app.errors.messages import ErrorMessage


class InternalServerErrorOut(BaseModel):
    """
    InternalServerErrorOut
    """
    detail: str = Field(default=ErrorMessage.INTERNAL_SERVER_ERROR)
    status_code: int = Field(default=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DuplicateArxivQueryOut(BaseModel):
    """
    DuplicateArxivQueryOut
    """
    detail: str = Field(default=ErrorMessage.DUPLICATE_ARXIV_QUERY)
    status_code: int = Field(default=status.HTTP_409_CONFLICT)
