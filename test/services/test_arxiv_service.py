from app.schemas import ArxivPaper, Author
from app.services import ArxivService


class TestArxivService():
    def test_get_papers(self):
        service = ArxivService()
        papers = service.search('deep learning')
        papers = list(papers)
        assert len(papers) > 0
        assert papers[0].title is not None
        assert papers[0].summary is not None
        assert papers[0].published is not None
        assert papers[0].authors is not None
