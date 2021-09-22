
from factory import Faker, Sequence
from factory.alchemy import SQLAlchemyModelFactory
from factory.declarations import SubFactory
from sqlalchemy import func

from app.factories import ArxivQueryFactory
from app.models import PaperModel, session


class PaperFactory(SQLAlchemyModelFactory):
    class Meta:

        model = PaperModel
        sqlalchemy_session = session

    title = Sequence(lambda n: f'title_{n}')
    abstract = Faker('text')
    abstract_jp = ""
    pdf_link = Faker('url')
    published_at = "2021/09/21"
    is_stocked = True
    arxiv_query_model = SubFactory(ArxivQueryFactory)
    created_at = func.now()
    updated_at = func.now()
