import time

import arxiv
import schedule
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import and_, exists

from app.jobs.job_logger import job_logger
from app.models import ArxivQueryModel, PaperModel, session


def get_search_result(keyword):
     # Arxiv APIから論文の一覧を取得
    search = arxiv.Search(
    query = keyword,
    sort_by = arxiv.SortCriterion.SubmittedDate,
    max_results = 50
    )

    # 保存処理

    search_results = [ i for i in search.results()]

    return search_results


def fetch_arxiv():

    try:
        # 検索ワードの取得
        arxiv_queries = session.query(ArxivQueryModel.arxiv_query_id,ArxivQueryModel.arxiv_query)\
        .filter(ArxivQueryModel.is_active == True)\
        .order_by(ArxivQueryModel.arxiv_query_id).all()

        need_commit = False

        for arxiv_query in arxiv_queries:

            search_results = get_search_result(arxiv_query['arxiv_query'])

            # submitted date を見て保存するかチェック
            for result in search_results:

                if session.query(exists().where(and_(PaperModel.arxiv_query_id == arxiv_query['arxiv_query_id'] ,
                                                PaperModel.pdf_link == result.pdf_url) )).scalar():
                    continue

                year, month , day = result.published.year,result.published.month,result.published.day

                paper_model = PaperModel(title=result.title,
                                        abstract=result.summary,
                                        abstract_jp="",
                                        pdf_link=result.pdf_url,
                                        published_at=f'{year}/{str(month).zfill(2)}/{str(day).zfill(2)}',
                                        arxiv_query_id=arxiv_query['arxiv_query_id'])

                session.add(paper_model)
                need_commit = True
        job_logger.info('log out put')
        if need_commit:
            session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        job_logger.error(e)
    except Exception as e:
        session.rollback()
        job_logger.error(e)


def main():

    schedule.every().day.at("23:00").do(fetch_arxiv)

    # schedule.every(1).minutes.do(fetch_arxiv)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
