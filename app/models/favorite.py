from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from app.models import BaseModel, PaperModel


class FavoriteModel(BaseModel):
    """
    FavoriteModel
    """
    __tablename__ = 'favorites'

    id: int = Column(Integer, primary_key=True)
    is_checked: bool = Column(Boolean, nullable=False, default=False)
    paper_id: int = Column(Integer, ForeignKey(PaperModel.id), nullable=False)
    paper: PaperModel = relationship(PaperModel)

    def __init__(self,
                 is_checked: bool,
                 paper_id: Optional[int]=None,
                 paper: Optional[PaperModel] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:

        if paper_id is not None:
            self.paper_id = paper_id
        if paper is not None:
            self.paper = paper
        self.is_checked = is_checked
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<FavoriteModel('%s', '%s', '%s','%s','%s')>" %\
            (self.id,
             self.paper_id,
             self.is_checked,
             self.created_at,
             self.updated_at)
