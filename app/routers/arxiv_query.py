from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import exists

from app.models import ArxivQueryModel, session
from app.request.arxiv_query import ArxivQueryDeleteIn, ArxivQueryPostIn, ArxivQueryPutIn
from app.response.arxiv_query import (ArxivQueryDeleteOut, ArxivQueryGetOut, ArxivQueryPostConflict, ArxivQueryPostOut,
                                      ArxivQueryPutNone, ArxivQueryPutOut)

router = APIRouter()

router = APIRouter(prefix="/arxiv_query",
                   tags=["arxiv_query"]
                   )


@router.get("/", summary="登録済みの検索クエリ一覧を取得", response_model=ArxivQueryGetOut)
async def fetch_all_arxiv_queries():
    pass


@router.post("/",
             summary="論文の検索クエリを登録",
             response_model=ArxivQueryPostOut,
             responses={status.HTTP_409_CONFLICT: {'description': '登録しようとしたArxivクエリが存在する場合',
                                                   'model': ArxivQueryPostConflict}})
async def save_arxiv_query(params: ArxivQueryPostIn):

    try:
        # 重複チェック
        if session.query(exists().where(ArxivQueryModel.arxiv_query == params.arxiv_query)).scalar():

            return JSONResponse(status_code=409, content={"message": "既に登録されています"})
        else:
            # 登録処理
            arxiv_query_model = ArxivQueryModel(arxiv_query=params.arxiv_query)
            session.add(arxiv_query_model)
            session.commit()
        return ArxivQueryPostOut()

    except SQLAlchemyError as e:
        session.rollback()

    except Exception as e:
        session.rollback()


@router.put("/",
            summary="論文検索時に使用するクエリの状態を更新",
            response_model=ArxivQueryPutOut,
            responses={status.HTTP_404_NOT_FOUND: {'description': '更新しようとしたidのレコードが存在しない場合',
                                                   'model': ArxivQueryPutNone}})
async def update_arxiv_query_is_active(params: ArxivQueryPutIn):

    try:
        record = session.query(ArxivQueryModel).filter(ArxivQueryModel.arxiv_query_id == params.arxiv_query_id).first()

        if record is None:
            return JSONResponse(status_code=404, content={"message": "更新対象が存在しませんでした"})

        else:
            record.is_active = not record.is_active
            session.commit()
        return ArxivQueryPutOut()
    except SQLAlchemyError as e:
        session.rollback()

    except Exception as e:
        session.rollback()


@ router.delete("/", summary="論文の検索クエリを削除する", response_model=ArxivQueryDeleteOut)
async def delete_arxiv_query(params: ArxivQueryDeleteIn):
    pass
