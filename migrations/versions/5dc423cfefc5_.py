"""empty message

Revision ID: 5dc423cfefc5
Revises: fe1e0e98f743
Create Date: 2016-11-02 06:15:39.736370

"""

# revision identifiers, used by Alembic.
revision = '5dc423cfefc5'
down_revision = 'fe1e0e98f743'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imei', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('results')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=Text()), autoincrement=False, nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'results_pkey')
    )
    op.drop_table('device')
    ### end Alembic commands ###
