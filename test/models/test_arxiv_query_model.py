from app.models import ArxivQueryModel
from app.models.factories import ArxivQueryFactory


class TestArxivQueryModel:

    def test__is_duplicated_is_true(self, db_session):
        """
        重複している場合のテスト
        """
        test_arxiv_query_model = ArxivQueryFactory.build()
        db_session.add(test_arxiv_query_model)
        db_session.commit()

        arxiv_query_model = ArxivQueryModel(arxiv_query=test_arxiv_query_model.arxiv_query)

        assert arxiv_query_model._is_duplicated(arxiv_query_model.arxiv_query) is True

    def test__is_duplicated_is_false(self):
        """
        重複していない場合のテスト
        """
        arxiv_query_model = ArxivQueryModel(arxiv_query="test")

        assert arxiv_query_model._is_duplicated(arxiv_query_model.arxiv_query) is False

    def test_save_is_true(self):
        """
        登録に成功した場合のテスト
        """
        arxiv_query_model = ArxivQueryFactory.build()

        assert arxiv_query_model.save() is True

    def test_save_is_false(self, db_session):
        """
        登録に失敗した場合のテスト
        """
        test_arxiv_query_model = ArxivQueryFactory.build()
        db_session.add(test_arxiv_query_model)
        db_session.commit()

        arxiv_query_model = ArxivQueryModel(arxiv_query=test_arxiv_query_model.arxiv_query)

        assert arxiv_query_model.save() is False
