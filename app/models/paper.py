from datetime import datetime
from typing import Optional

from sqlalchemy import TEXT, Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey, UniqueConstraint

from app.models.query import QueryModel
from app.models.setting import BaseModel


class PaperModel(BaseModel):
    """
    PaperModel
    """
    __tablename__ = 'papers'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(TEXT, nullable=False)
    abstract: str = Column(TEXT, nullable=False)
    link: str = Column(TEXT, nullable=False)
    query_id: int = Column(Integer, ForeignKey(QueryModel.id), nullable=False)
    query: QueryModel = relationship(QueryModel)

    def __init__(self,
                 title: str,
                 abstract: str,
                 link: str,
                 quey_id: Optional[int] = None,
                 query: Optional[QueryModel] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.title = title
        self.abstract = abstract
        self.link = link
        if quey_id is not None:
            self.query_id = quey_id
        if query is not None:
            self.query = query
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<PaperModel('%s', '%s', '%s','%s','%s','%s','%s')>" %\
            (self.id,
             self.title,
             self.abstract,
             self.link,
             self.query_id,
             self.created_at,
             self.updated_at)
