from typing import List, Optional

from pydantic import BaseModel


class Paper(BaseModel):
    """/papers get の各論文情報を保持するクラス

    Attributes:

        created_at (str): 登録日時(YYYY/MM/DD)

        arxiv_query_id (int): ArxivクエリID

        is_stocked (bool): ストック判定フラグ

        is_checked (bool): ストックした論文でチェック済みか判定するフラグ

        title (str): 論文のタイトル

        abstract (str): 論文の概要

    """

    created_at: str
    arxiv_query_id: int
    is_stocked: bool
    is_checked: bool
    title: str
    abstract: str

    class Config:
        schema_extra = {
            'example': {'created_at': '2021/09/23',
                        'arxiv_query_id': 1,
                        'is_stocked': True,
                        'is_checked': False,
                        'title': 'paper title',
                        'abstract': 'paper abstract'}
        }


class PapersGetOut(BaseModel):
    """/papers get レスポンスクラス

    Attributes:

        papers (list[Paper]): PaperのList

        current_page (int): ページネーションの表示するページ

        all_page_size (int): ページネーションの全てのページサイズ

    """

    papers: List[Paper]
    current_page: int
    all_page_size: int

    class Config:
        schema_extra = {
            'example': {
                'papers': [
                    {'created_at': '2021/09/23',
                        'arxiv_query_id': 1,
                        'is_stocked': True,
                        'is_checked': False,
                        'title': 'paper title 1',
                        'abstract': 'paper abstract 1'},
                    {'created_at': '2021/09/23',
                        'arxiv_query_id': 1,
                        'is_stocked': True,
                        'is_checked': True,
                        'title': 'paper title 2',
                        'abstract': 'paper abstract 2'}
                ],
                'current_page': 1,
                'all_page_size': 1,
            }
        }
