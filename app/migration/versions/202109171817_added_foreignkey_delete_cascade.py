"""Added foreignkey delete cascade

Revision ID: 5d8c9b5cc038
Revises: a2fa793538c6
Create Date: 2021-09-17 18:17:09.520314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d8c9b5cc038'
down_revision = 'a2fa793538c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_paper_stocks_paper_id_papers', 'paper_stocks', type_='foreignkey')
    op.create_foreign_key(op.f('fk_paper_stocks_paper_id_papers'), 'paper_stocks', 'papers', ['paper_id'], ['paper_id'], ondelete='CASCADE')
    op.drop_constraint('fk_papers_arxiv_query_id_arxiv_queries', 'papers', type_='foreignkey')
    op.create_foreign_key(op.f('fk_papers_arxiv_query_id_arxiv_queries'), 'papers', 'arxiv_queries', ['arxiv_query_id'], ['arxiv_query_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_papers_arxiv_query_id_arxiv_queries'), 'papers', type_='foreignkey')
    op.create_foreign_key('fk_papers_arxiv_query_id_arxiv_queries', 'papers', 'arxiv_queries', ['arxiv_query_id'], ['arxiv_query_id'])
    op.drop_constraint(op.f('fk_paper_stocks_paper_id_papers'), 'paper_stocks', type_='foreignkey')
    op.create_foreign_key('fk_paper_stocks_paper_id_papers', 'paper_stocks', 'papers', ['paper_id'], ['paper_id'])
    # ### end Alembic commands ###