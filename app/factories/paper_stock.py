from factory.alchemy import SQLAlchemyModelFactory
from factory.declarations import SubFactory
from sqlalchemy import func

from app.factories import PaperFactory
from app.models import PaperStockModel, session


class PaperStockFactory(SQLAlchemyModelFactory):
    class Meta:

        model = PaperStockModel
        sqlalchemy_session = session

    is_checked = False
    paper_model = SubFactory(PaperFactory)
    created_at = func.now()
    updated_at = func.now()
