from fastapi import APIRouter

from app.request.paper import PapersGetIn
from app.response.paper import PapersGetOut

router = APIRouter()

router = APIRouter(
    prefix="/papers",
    tags=["papers"]
)


@router.get("/", summary="論文の一覧を取得", response_model=PapersGetOut)
async def get_papers(params: PapersGetIn):
    pass
