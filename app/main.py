from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models.setting import initialize_db
from app.routers import arxiv_query_router, paper_stock_router, papers_router

app = FastAPI(title="FastAPI Template", version="1.0.0")

app.include_router(arxiv_query_router)
app.include_router(papers_router)
app.include_router(paper_stock_router)

initialize_db()

origins = [
    "https://localhost",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
