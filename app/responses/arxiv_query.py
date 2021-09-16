from typing import List

from pydantic import BaseModel, Field


class ArxivQuery(BaseModel):
    """arxiv_queryのクエリひとつを表すクラス

    Attributes:

        arxiv_query_id (int): ArxivクエリID

        arxiv_query (str): Arxivクエリ

        is_active (str): 論文検索時に使用するクエリか判定するフラグ
    """
    arxiv_query_id: int
    arxiv_query: str
    is_active: bool

    class Config:
        schema_extra = {
            'example': {'arxiv_query_id': 1, 'arxiv_query': 'OCR', 'is_active': True}
        }


class ArxivQueryGetOut(BaseModel):
    """/arxiv_query get レスポンスクラス

    Attributes:

        arxiv_queries (list[ArxivQuery]): ArxivQueryのList
    """

    arxiv_queries: List[ArxivQuery]

    class Config:
        schema_extra = {
            'example': {
                'arxiv_queries': [{'arxiv_query_id': 1, 'arxiv_query': 'OCR', 'is_active': True},
                                  {'arxiv_query_id': 2, 'arxiv_query': 'FaceRecognition', 'is_active': True}
                                  ]
            }
        }


class ArxivQueryPostOut(BaseModel):
    """/arxiv_query post レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field(..., title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': '検索クエリの登録が完了しました'
            }
        }


class ArxivQueryPutOut(BaseModel):
    """/arxiv_query put レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field(..., title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': '検索クエリの更新が完了しました'
            }
        }


class ArxivQueryDeleteOut(BaseModel):
    """/arxiv_query delete レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field(..., title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': '検索クエリの削除が完了しました'
            }
        }
