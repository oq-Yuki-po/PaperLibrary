from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer, String

from app.models import BaseModel


class QueryModel(BaseModel):
    """
    QueryModel
    """
    __tablename__ = 'queries'

    id: int = Column(Integer, primary_key=True)
    query: str = Column(String(255), nullable=False, unique=True)
    is_delted: bool = Column(Boolean, nullable=False, default=False)

    def __init__(self,
                 query: str,
                 is_deleted: bool,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.query = query
        self.is_delted = is_deleted
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<QueryModel('%s', '%s', '%s','%s','%s')>" %\
            (self.id,
             self.query,
             self.is_delted,
             self.created_at,
             self.updated_at)
