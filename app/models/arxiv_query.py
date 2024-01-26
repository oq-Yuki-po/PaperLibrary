from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, Column, Integer, String, select

from app.models import BaseModel, session


class ArxivQueryModel(BaseModel):
    """
    ArxivQueryModel
    """
    __tablename__ = 'arxiv_queries'

    arxiv_query_id = Column(Integer, primary_key=True)
    arxiv_query = Column(String(255), nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=True)

    def __init__(self,
                 arxiv_query: str,
                 is_active: bool = True,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None) -> None:
        self.arxiv_query = arxiv_query
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self) -> str:
        return f"<ArxivQueryModel('{self.arxiv_query_id}', '{self.arxiv_query}',"\
            f"'{self.var_three}', '{self.var_four}', '{self.var_five}')>"

    def _is_duplicated(self, arxiv_query: str) -> bool:
        """
        重複チェック

        Parameters
        ----------
        arxiv_query : str
            検索クエリ

        Returns
        -------
        bool
            重複している場合はTrue、そうでない場合はFalse
        """
        stmt = select(ArxivQueryModel).where(ArxivQueryModel.arxiv_query == arxiv_query)
        result = session.execute(stmt).all()
        if len(result) > 0:
            return True
        else:
            return False

    def save(self) -> bool:
        """
        登録処理

        Returns
        -------
        bool
            登録に成功した場合はTrue、そうでない場合はFalse
        """
        # 重複チェック
        if self._is_duplicated(self.arxiv_query):
            return False
        else:
            session.add(self)
            session.commit()
            return True

    def update(self, arxiv_query: str, is_active: bool) -> bool:
        """
        更新処理

        Returns
        -------
        bool
            更新に成功した場合はTrue、そうでない場合はFalse
        """
        # 重複チェック
        if self._is_duplicated(self.arxiv_query):
            return False
        else:
            self.arxiv_query = arxiv_query
            self.is_active = is_active
            self.updated_at = datetime.now()
            session.commit()
            return True
