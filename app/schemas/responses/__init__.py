from app.schemas.responses.arxiv_query import (
    ArxivQuery,
    ArxivQueryDeleteOut,
    ArxivQueryGetOut,
    ArxivQueryPostConflict,
    ArxivQueryPostOut,
    ArxivQueryPutNone,
    ArxivQueryPutOut,
)
from app.schemas.responses.error import (
    DataBaseConnectionError,
    DataBaseConnectionErrorOut,
    DataBaseError,
    DataBaseErrorOut,
    ErrorMessage,
    InternalServerError,
    InternalServerErrorOut,
    InvalidRequestError,
    InvalidRequestErrorOut,
)
from app.schemas.responses.paper import PapersGetOut
from app.schemas.responses.paper_stock import PaperStockDeleteOut, PaperStockPostOut, PaperStockPutOut
