from typing import List

from pydantic import BaseModel, Field


class PaperStockPostOut(BaseModel):
    """/paper_stock post レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field('論文のストックが完了しました', title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': '論文のストックが完了しました'
            }
        }


class PaperStockPutOut(BaseModel):
    """/paper_stock put レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field('ストックしている論文のステータスを更新しました', title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': 'ストックしている論文のステータスを更新しました'
            }
        }


class PaperStockDeleteOut(BaseModel):
    """/paper_stock put レスポンスクラス

    Attributes:

        message (str): メッセージ
    """
    message: str = Field('論文をストックから削除しました', title='message')

    class Config:
        schema_extra = {
            'example': {
                'message': '論文をストックから削除しました'
            }
        }
