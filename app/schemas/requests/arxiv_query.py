from pydantic import BaseModel, ConfigDict, Field


class ArxivQueryPostIn(BaseModel):
    """/arxiv_query post リクエストクラス

    Attributes:

        arxiv_query (str): 論文検索時に使用するクエリ
    """

    arxiv_query: str = Field(...,
                             min_length=1,
                             max_length=255)

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            'example': {
                'arxiv_query': 'OCR'
            }
        }
    )


class ArxivQueryPutIn(BaseModel):
    """/arxiv_query put リクエストクラス

    Attributes:

        arxiv_query_id (int): ArxivクエリID
    """
    arxiv_query_id: int = Field(...)

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            'example': {
                'arxiv_query_id': 10
            }
        }
    )


class ArxivQueryDeleteIn(BaseModel):
    """/arxiv_query delete リクエストクラス

    Attributes:

        arxiv_query_id (int): ArxivクエリID
    """
    arxiv_query_id: int = Field(...)

    model_config: ConfigDict = ConfigDict(
        json_schema_extra={
            'example': {
                'arxiv_query_id': 10
            }
        }
    )
