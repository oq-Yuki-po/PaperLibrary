from fastapi import APIRouter

from app.request.arxiv_query import ArxivQueryDeleteIn, ArxivQueryPostIn, ArxivQueryPutIn
from app.response.arxiv_query import ArxivQueryDeleteOut, ArxivQueryGetOut, ArxivQueryPostOut, ArxivQueryPutOut

router = APIRouter()

router = APIRouter(prefix="/arxiv_query",
                   tags=["arxiv_query"]
                   )


@router.get("/", summary="登録済みの検索クエリ一覧を取得", response_model=ArxivQueryGetOut)
async def fetch_all_arxiv_queries():
    pass


@router.post("/", summary="論文の検索クエリを登録", response_model=ArxivQueryPostOut)
async def save_arxiv_query(params: ArxivQueryPostIn):
    pass


@router.put("/", summary="論文検索時に使用するクエリの状態を更新", response_model=ArxivQueryPutOut)
async def update_arxiv_query_is_active(params: ArxivQueryPutIn):
    pass


@router.delete("/", summary="論文の検索クエリを削除する", response_model=ArxivQueryDeleteOut)
async def delete_arxiv_query(params: ArxivQueryDeleteIn):
    pass
