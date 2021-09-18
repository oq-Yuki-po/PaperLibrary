import pytest
from fastapi import status

from app.factories import ArxivQueryFactory
from app.models import ArxivQueryModel, session


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


class TestArxivQueryPut():

    @pytest.mark.parametrize("init_is_active", [True, False])
    def test_update_arxiv_query_is_active(self, app_client, db_session, init_is_active):

        arxiv_query_model = ArxivQueryFactory(is_active=init_is_active)

        db_session.add(arxiv_query_model)
        db_session.commit()

        arxiv_query_model = db_session.query(ArxivQueryModel).all()

        assert len(arxiv_query_model) == 1
        assert arxiv_query_model[0].is_active is init_is_active

        id = arxiv_query_model[0].arxiv_query_id
        response = app_client.put("/arxiv_query/", json={"arxiv_query_id": id})

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "検索クエリの更新が完了しました"}

        arxiv_query_model = db_session.query(ArxivQueryModel).\
            filter(ArxivQueryModel.arxiv_query_id == id).\
            first()

        assert arxiv_query_model.is_active is not init_is_active

    def test_update_arxiv_query_is_active_none(self, app_client, db_session):
        id = 100
        response = app_client.put("/arxiv_query/", json={"arxiv_query_id": id})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"message": "更新対象が存在しませんでした"}
