from fastapi import APIRouter

from app.models import PaperModel, session
from app.response.paper_stock import PaperStockPutOut

router = APIRouter()

router = APIRouter(
    prefix="/paper_stock",
    tags=["paper_stock"]
)



@router.put("/{paper_id}", summary="論文のストックのステータスを更新", response_model=PaperStockPutOut)
async def update_papers_is_stocked(paper_id):

    paper_model = session.query(PaperModel).filter(PaperModel.paper_id==paper_id).first()

    paper_model.is_stocked = not paper_model.is_stocked

    session.commit()

    return PaperStockPutOut()
