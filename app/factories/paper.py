
from factory import Faker, Sequence
from factory.alchemy import SQLAlchemyModelFactory
from factory.declarations import SubFactory
from sqlalchemy import func

from app.factories import QueryFactory
from app.models import PaperModel, session


class PaperFactory(SQLAlchemyModelFactory):
    class Meta:

        model = PaperModel
        sqlalchemy_session = session

    title = Sequence(lambda n: f'title_{n}')
    abstract = Faker('text')
    link = Faker('url')
    query = SubFactory(QueryFactory)
    created_at = func.now()
    updated_at = func.now()
