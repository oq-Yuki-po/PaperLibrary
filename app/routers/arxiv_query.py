from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.sql import exists

from app.errors import DuplicateArxivQuery
from app.models import ArxivQueryModel, session
from app.schemas.errors import DuplicateArxivQueryOut
from app.schemas.requests import ArxivQueryDeleteIn, ArxivQueryPostIn, ArxivQueryPutIn
from app.schemas.responses import (
    ArxivQuery,
    ArxivQueryDeleteOut,
    ArxivQueryGetOut,
    ArxivQueryPostConflict,
    ArxivQueryPostOut,
    ArxivQueryPutNone,
    ArxivQueryPutOut,
)

router = APIRouter()

router = APIRouter(prefix="/arxiv_query",
                   tags=["arxiv_query"]
                   )


@router.get("/", summary="登録済みの検索クエリ一覧を取得", response_model=ArxivQueryGetOut)
async def fetch_all_arxiv_queries():

    arxiv_queries = session.query(ArxivQueryModel.arxiv_query_id,
                                  ArxivQueryModel.arxiv_query,
                                  ArxivQueryModel.is_active).order_by(ArxivQueryModel.arxiv_query_id).all()

    return ArxivQueryGetOut(arxiv_queries=[ArxivQuery(arxiv_query_id=i.arxiv_query_id,
                                                      arxiv_query=i.arxiv_query,
                                                      is_active=i.is_active) for i in arxiv_queries])


@router.post("/",
             summary="論文の検索クエリを登録",
             response_model=ArxivQueryPostOut,
             responses={status.HTTP_409_CONFLICT: {'description': '登録しようとしたArxivクエリが存在する場合',
                                                   'model': DuplicateArxivQueryOut}})
async def save_arxiv_query(params: ArxivQueryPostIn):

    arxiv_model = ArxivQueryModel(arxiv_query=params.arxiv_query)

    if arxiv_model.save() is False:
        raise DuplicateArxivQuery()

    return ArxivQueryPostOut(saved_query=ArxivQuery(arxiv_query_id=arxiv_model.arxiv_query_id,
                                                    arxiv_query=arxiv_model.arxiv_query,
                                                    is_active=arxiv_model.is_active))


@router.put("/",
            summary="論文検索時に使用するクエリの状態を更新",
            response_model=ArxivQueryPutOut,
            responses={status.HTTP_404_NOT_FOUND: {'description': '更新しようとしたidのレコードが存在しない場合',
                                                   'model': ArxivQueryPutNone}})
async def update_arxiv_query_is_active(params: ArxivQueryPutIn):

    record = session.query(ArxivQueryModel).filter(ArxivQueryModel.arxiv_query_id == params.arxiv_query_id).first()

    if record is None:
        return JSONResponse(status_code=404, content={"message": "更新対象が存在しませんでした"})

    else:
        record.is_active = not record.is_active
        session.commit()
    return ArxivQueryPutOut()


@ router.delete("/", summary="論文の検索クエリを削除する", response_model=ArxivQueryDeleteOut)
async def delete_arxiv_query(params: ArxivQueryDeleteIn):

    session.query(ArxivQueryModel).filter(ArxivQueryModel.arxiv_query_id == params.arxiv_query_id).delete()

    session.commit()

    return ArxivQueryDeleteOut()
