from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class PapersGetIn(BaseModel):
    """/papers get リクエストクラス

    Attributes:

        published_at (str): 論文の公開日時(YYYY/MM/DD)

        arxiv_query_id (int): ArxivクエリID

        is_stocked (bool): ストックのみを表示するか判定するフラグ

        page (int): ページネーションに使用する表示したいページ数

    """

    published_at: List[str] = Field([str(datetime.now().strftime("%Y/%m/%d")),
                                     str(datetime.now().strftime("%Y/%m/%d"))])
    arxiv_query_id: Optional[int]
    is_stocked: Optional[bool] = Field(False)
    page: int = Field(1)

    class Config:
        schema_extra = {
            'example': {
                'published_at': ['2021/09/20', '2021/09/24'],
                'arxiv_query_id': 1,
                'is_stocked': True,
                'page': 1
            }
        }
