from fastapi import APIRouter
from sqlalchemy import desc, func, over

from app.models import ArxivQueryModel, PaperModel, session
from app.schemas.requests import PapersGetIn
from app.schemas.responses import PapersGetOut

router = APIRouter()

router = APIRouter(
    prefix="/papers",
    tags=["papers"]
)


@router.post("/", summary="論文の一覧を取得", response_model=PapersGetOut)
async def get_papers(params: PapersGetIn):
    start_published_at, end_published_at = params.published_at
    arxiv_query_id = params.arxiv_query_id
    is_stocked = params.is_stocked
    page = params.page
    page_size = 6

    query = session.query(ArxivQueryModel.arxiv_query_id.label('arxiv_query_id'),
                          PaperModel.paper_id.label('paper_id'),
                          PaperModel.title.label('title'),
                          PaperModel.is_stocked.label('is_stocked'),
                          PaperModel.abstract.label('abstract'),
                          PaperModel.pdf_link.label('pdf_link'),
                          PaperModel.published_at.label('published_at'),
                          over(func.count()).label('all_page_count')
                          ).outerjoin(PaperModel,
                                      ArxivQueryModel.arxiv_query_id == PaperModel.arxiv_query_id
                                      )

    if (start_published_at != '') and (end_published_at != ''):
        query = query.filter(PaperModel.published_at.between(start_published_at, end_published_at))

    if arxiv_query_id != 0:
        query = query.filter(ArxivQueryModel.arxiv_query_id == arxiv_query_id)

    if is_stocked:
        query = query.filter(PaperModel.is_stocked == is_stocked)

    query_results = query.group_by(ArxivQueryModel.arxiv_query_id,
                                   PaperModel.paper_id,
                                   PaperModel.title,
                                   PaperModel.is_stocked,
                                   PaperModel.abstract,
                                   PaperModel.pdf_link,
                                   PaperModel.published_at)\
        .order_by(desc(PaperModel.published_at)).limit(page_size).offset((page - 1) * page_size).all()

    papers = []

    for paper in query_results:
        papers.append(Paper(published_at=paper.published_at.strftime("%Y/%m/%d"),
                            arxiv_query_id=paper.arxiv_query_id,
                            is_stocked=paper.is_stocked,
                            title=paper.title,
                            abstract=paper.abstract,
                            pdf_link=paper.pdf_link,
                            paper_id=paper.paper_id))
    if len(query_results) == 0:
        return PapersGetOut(papers=[], current_page=page, all_page_size=0)
    else:

        records_count = query_results[0].all_page_count
        all_page_size = records_count // page_size if records_count % page_size == 0 else records_count // page_size + 1

        return PapersGetOut(papers=papers, current_page=page, all_page_size=all_page_size)
