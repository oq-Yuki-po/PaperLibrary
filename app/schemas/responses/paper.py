from typing import List

from pydantic import BaseModel, ConfigDict


class Paper(BaseModel):
    """/papers get の各論文情報を保持するクラス

    Attributes:

        published_at (str): 論文の公開日時(YYYY/MM/DD)

        paper_id (int): PaperID

        arxiv_query_id (int): ArxivクエリID

        is_stocked (bool): ストック判定フラグ

        title (str): 論文のタイトル

        abstract (str): 論文の概要

        pdf_link (str): padリンク

    """

    published_at: str
    paper_id: int
    arxiv_query_id: int
    is_stocked: bool
    title: str
    abstract: str
    pdf_link: str

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            'example': {'published_at': '2021/09/23',
                        'paper_id': 2,
                        'arxiv_query_id': 1,
                        'is_stocked': True,
                        'title': 'paper title',
                        'abstract': 'paper abstract',
                        'pdf_link': 'sample.pdf'}
        }
    )


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

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            'example': {
                'papers': [
                    {'published_at': '2021/09/23',
                     'paper_id': 2,
                     'arxiv_query_id': 1,
                     'is_stocked': True,
                     'title': 'paper title 1',
                     'abstract': 'paper abstract 1',
                     'pdf_link': 'sample_1.pdf'},
                    {'published_at': '2021/09/23',
                     'paper_id': 3,
                     'arxiv_query_id': 1,
                     'is_stocked': True,
                     'title': 'paper title 2',
                     'abstract': 'paper abstract 2',
                     'pdf_link': 'sample_2.pdf'}
                ],
                'current_page': 1,
                'all_page_size': 1,
            }
        }
    )
