from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import ForeignKey

from app.models import BaseModel, PaperModel


class PaperStockModel(BaseModel):
    """
    PaperStockModel
    """
    __tablename__ = 'paper_stocks'

    paper_stock_id: int = Column(Integer, primary_key=True)
    is_checked: bool = Column(Boolean, nullable=False, default=False)
    paper_id: int = Column(Integer, ForeignKey(PaperModel.paper_id, ondelete='CASCADE'), nullable=False)
    paper_model: PaperModel = relationship(PaperModel, backref=backref('paper_stocks', passive_deletes=True))

    def __init__(self,
                 is_checked: bool,
                 paper_id: Optional[int] = None,
                 paper_model: Optional[PaperModel] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:

        if paper_id is not None:
            self.paper_id = paper_id
        if paper_model is not None:
            self.paper_model = paper_model
        self.is_checked = is_checked
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<PaperStockModel('%s', '%s', '%s','%s','%s')>" %\
            (self.paper_stock_id,
             self.paper_id,
             self.is_checked,
             self.created_at,
             self.updated_at)
