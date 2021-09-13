
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy import func

from app.models import QueryModel, session


class QueryFactory(SQLAlchemyModelFactory):
    class Meta:

        model = QueryModel
        sqlalchemy_session = session

    query = Sequence(lambda n: f'query_{n}')
    is_deleted = False
    created_at = func.now()
    updated_at = func.now()
