from fastapi import APIRouter

from app.response.paper_stock import PaperStockDeleteOut, PaperStockPostOut, PaperStockPutOut

router = APIRouter()

router = APIRouter(
    prefix="/paper_stock",
    tags=["paper_stock"]
)



@router.post("/{paper_id}", summary="ストックする論文を登録", response_model=PaperStockPostOut)
async def save_paper_stock():
    pass


@router.put("/{paper_id}", summary="ストックしている論文のステータスを更新", response_model=PaperStockPutOut)
async def update_paper_stock_is_checked():
    pass

@router.delete("/{paper_id}", summary="論文をストックから削除", response_model=PaperStockDeleteOut)
async def delete_paper_stock():
    pass
