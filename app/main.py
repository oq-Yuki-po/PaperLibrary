from fastapi import FastAPI

from app.models.setting import initialize_db
from app.routers import arxiv_query_router, paper_stock_router, papers_router

app = FastAPI(title="FastAPI Template", version="1.0.0")

app.include_router(arxiv_query_router)
app.include_router(papers_router)
app.include_router(paper_stock_router)

initialize_db()
