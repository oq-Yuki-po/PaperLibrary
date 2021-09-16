
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy import func

from app.models import ArxivQueryModel, session


class ArxivQueryFactory(SQLAlchemyModelFactory):
    class Meta:

        model = ArxivQueryModel
        sqlalchemy_session = session

    arxiv_query = Sequence(lambda n: f'arxiv_query_{n}')
    is_active = True
    created_at = func.now()
    updated_at = func.now()
