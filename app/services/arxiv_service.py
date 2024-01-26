import arxiv
from arxiv.arxiv import Result


class ArxivService():

    def __init__(self):
        self.client = arxiv.Client()

    def search(self, query):
        search = arxiv.Search(
            query=query,
            max_results=10,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        return self.client.results(search)

    def download(self, paper: Result):
        return paper.download_source(dirpath="./tmp")
