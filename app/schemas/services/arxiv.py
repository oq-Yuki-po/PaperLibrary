from datetime import datetime
from typing import List

from pydantic import BaseModel, field_validator


class Author(BaseModel):
    name: str


class ArxivPaper(BaseModel):
    entry_id: str
    title: str
    summary: str
    published: datetime

    @field_validator('published')
    def datetime_to_str(cls, v):  # pylint:disable=E0213
        if isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return v
    authors: List[Author]
