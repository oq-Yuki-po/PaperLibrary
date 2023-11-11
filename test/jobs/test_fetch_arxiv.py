import pickle

from app.jobs.fetch_arxiv import fetch_arxiv
from app.models import ArxivQueryModel, PaperModel
from app.models.factories import ArxivQueryFactory


def test_fetch_arxiv(db_session, mocker):

    # 前処理
    with open('test/search_results.pickle', 'rb') as f:
        search_results = pickle.load(f)

    mocker.patch('app.jobs.fetch_arxiv.get_search_result', return_value=search_results)

    target_query = "OCR"

    arxiv_query_model = ArxivQueryFactory(arxiv_query=target_query, is_active=True)

    db_session.add(arxiv_query_model)
    db_session.commit()

    fetch_arxiv()

    # 確認

    paper_models = db_session.query(ArxivQueryModel, PaperModel)\
        .outerjoin(PaperModel, ArxivQueryModel.arxiv_query_id == PaperModel.arxiv_query_id)\
        .filter(ArxivQueryModel.arxiv_query_id == arxiv_query_model.arxiv_query_id)\
        .order_by(ArxivQueryModel.arxiv_query_id).all()

    assert len(paper_models) == len(search_results)
