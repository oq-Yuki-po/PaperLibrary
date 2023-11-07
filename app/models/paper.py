from datetime import datetime
from typing import Optional

from sqlalchemy import TEXT, Boolean, Column, Date, Integer
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import ForeignKey

from app.models import ArxivQueryModel, BaseModel


class PaperModel(BaseModel):
    """
    PaperModel
    """
    __tablename__ = 'papers'

    paper_id = Column(Integer, primary_key=True)
    title = Column(TEXT, nullable=False)
    abstract = Column(TEXT, nullable=False)
    abstract_jp = Column(TEXT, nullable=False)
    pdf_link = Column(TEXT, nullable=False)
    published_at = Column(Date, nullable=False)
    is_stocked = Column(Boolean, nullable=False, default=False)
    arxiv_query_id = Column(Integer,
                            ForeignKey(ArxivQueryModel.arxiv_query_id, ondelete='CASCADE'),
                            nullable=False)
    arxiv_query_model = relationship(ArxivQueryModel, backref=backref('papers', passive_deletes=True))

    def __init__(self,
                 title: str,
                 abstract: str,
                 abstract_jp: str,
                 pdf_link: str,
                 published_at: str,
                 is_stocked: bool = False,
                 arxiv_query_id: Optional[int] = None,
                 arxiv_query_model: Optional[ArxivQueryModel] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.title = title
        self.abstract = abstract
        self.abstract_jp = abstract_jp
        self.pdf_link = pdf_link
        self.published_at = published_at
        self.is_stocked = is_stocked
        if arxiv_query_id is not None:
            self.arxiv_query_id = arxiv_query_id
        if arxiv_query_model is not None:
            self.arxiv_query_model = arxiv_query_model
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return "<PaperModel('%s', '%s', '%s', '%s','%s','%s','%s','%s')>" %\
            (self.paper_id,
             self.title,
             self.abstract,
             self.abstract_jp,
             self.pdf_link,
             self.published_at,
             self.arxiv_query_id,
             self.created_at,
             self.updated_at)
