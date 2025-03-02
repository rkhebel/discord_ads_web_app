"""empty message

Revision ID: 69442ca1d943
Revises: a94de582d1ff
Create Date: 2021-01-19 15:46:54.855174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69442ca1d943'
down_revision = 'a94de582d1ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('advertisements', sa.Column('tags', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('advertisements', 'tags')
    # ### end Alembic commands ###
