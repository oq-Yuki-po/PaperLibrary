from factory.alchemy import SQLAlchemyModelFactory
from factory.declarations import SubFactory
from sqlalchemy import func

from app.factories import PaperFactory
from app.models import FavoriteModel, session


class FavoriteFactory(SQLAlchemyModelFactory):
    class Meta:

        model = FavoriteModel
        sqlalchemy_session = session

    is_checked = False
    paper = SubFactory(PaperFactory)
    created_at = func.now()
    updated_at = func.now()
