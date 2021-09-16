from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer, String

from app.models import BaseModel


class ArxivQueryModel(BaseModel):
    """
    ArxivQueryModel
    """
    __tablename__ = 'arxiv_queries'

    arxiv_query_id: int = Column(Integer, primary_key=True)
    arxiv_query: str = Column(String(255), nullable=False, unique=True)
    is_active: bool = Column(Boolean, nullable=False, default=True)

    def __init__(self,
                 arxiv_query: str,
                 is_active: bool,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.arxiv_query = arxiv_query
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<ArxivQueryModel('%s', '%s', '%s','%s','%s')>" %\
            (self.arxiv_query_id,
             self.arxiv_query,
             self.is_active,
             self.created_at,
             self.updated_at)
