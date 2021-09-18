import ast

from fastapi import status

from app.models import ArxivQueryModel


class TestArxivQueryPost():

    def test_fetch_all_arxiv_queries(self, app_client, db_session):

        target_query = "OCR"

        response = app_client.post("/arxiv_query/", json={"arxiv_query": target_query})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "検索クエリの登録が完了しました"}

        arxiv_query_model = db_session.query(ArxivQueryModel).\
            filter(ArxivQueryModel.arxiv_query == target_query).\
            all()

        assert len(arxiv_query_model) == 1
        assert arxiv_query_model[0].is_active
