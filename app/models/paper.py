from datetime import datetime
from typing import Optional

from sqlalchemy import TEXT, Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from app.models import ArxivQueryModel, BaseModel


class PaperModel(BaseModel):
    """
    PaperModel
    """
    __tablename__ = 'papers'

    paper_id: int = Column(Integer, primary_key=True)
    title: str = Column(TEXT, nullable=False)
    abstract: str = Column(TEXT, nullable=False)
    abstract_jp: str = Column(TEXT, nullable=False)
    pdf_link: str = Column(TEXT, nullable=False)
    arxiv_query_id: int = Column(Integer, ForeignKey(ArxivQueryModel.arxiv_query_id), nullable=False)
    arxiv_query_model: ArxivQueryModel = relationship(ArxivQueryModel)

    def __init__(self,
                 title: str,
                 abstract: str,
                 abstract_jp: str,
                 pdf_link: str,
                 arxiv_quey_id: Optional[int] = None,
                 arxiv_query_model: Optional[ArxivQueryModel] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.title = title
        self.abstract = abstract
        self.abstract_jp = abstract_jp
        self.pdf_link = pdf_link
        if arxiv_quey_id is not None:
            self.arxiv_quey_id = arxiv_quey_id
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
             self.arxiv_quey_id,
             self.created_at,
             self.updated_at)
