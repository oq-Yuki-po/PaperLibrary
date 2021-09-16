from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PapersGetIn(BaseModel):
    """/papers get リクエストクラス

    Attributes:

        created_at (str): 登録日時(YYYY/MM/DD)

        arxiv_query_id (int): ArxivクエリID

        is_stocked (bool): ストック判定フラグ

        page (int): ページネーションに使用する表示したいページ数

    """

    created_at: Optional[str] = Field(datetime.now().strftime("%Y/%m/%d"))
    arxiv_query_id: Optional[int]
    is_stocked: Optional[bool] = Field(False)
    page: int = Field(1)

    class Config:
        schema_extra = {
            'example': {
                'created_at': '2021/09/24',
                'arxiv_query_id': 2,
                'is_stocked': True,
                'page': 2
            }
        }
