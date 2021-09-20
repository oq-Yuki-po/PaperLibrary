import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app import app_logger
from app.models import session
from app.models.setting import initialize_db
from app.routers import arxiv_query_router, paper_stock_router, papers_router

app = FastAPI(title="FastAPI Template", version="1.0.0")

app.include_router(arxiv_query_router)
app.include_router(papers_router)
app.include_router(paper_stock_router)

initialize_db()

origins = [
    "https://localhost",
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_request_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
    except SQLAlchemyError as e:
        session.rollback()
        app_logger.error(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": "サーバー内で予期しないエラーが発生"})

    except Exception as e:
        session.rollback()
        app_logger.error(e)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content={"message": "サーバー内で予期しないエラーが発生"})
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
