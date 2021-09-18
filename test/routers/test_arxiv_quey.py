from fastapi import status

from app.factories import ArxivQueryFactory
from app.models import ArxivQueryModel


class TestArxivQueryPost():

    def test_save_arxiv_query(self, app_client, db_session):

        target_query = "OCR"

        response = app_client.post("/arxiv_query/", json={"arxiv_query": target_query})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "検索クエリの登録が完了しました"}

        arxiv_query_model = db_session.query(ArxivQueryModel).\
            filter(ArxivQueryModel.arxiv_query == target_query).\
            all()

        assert len(arxiv_query_model) == 1
        assert arxiv_query_model[0].is_active

    def test_save_arxiv_query_conflict(self, app_client, db_session):

        target_query = "OCR"

        arxiv_query_model = ArxivQueryFactory(arxiv_query=target_query)

        db_session.add(arxiv_query_model)
        db_session.commit()

        arxiv_query_model = db_session.query(ArxivQueryModel).all()

        assert len(arxiv_query_model) == 1

        response = app_client.post("/arxiv_query/", json={"arxiv_query": target_query})

        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.json() == {"message": "既に登録されています"}

        arxiv_query_model = db_session.query(ArxivQueryModel).all()
        assert len(arxiv_query_model) == 1
