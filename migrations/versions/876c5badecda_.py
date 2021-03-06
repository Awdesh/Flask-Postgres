"""empty message

Revision ID: 876c5badecda
Revises: None
Create Date: 2016-11-08 00:59:15.857425

"""

# revision identifiers, used by Alembic.
revision = '876c5badecda'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imei', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('serial', sa.BigInteger(), nullable=True),
    sa.Column('sim', sa.BigInteger(), nullable=True),
    sa.Column('realm', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('height', sa.String(), nullable=True),
    sa.Column('address1', sa.String(), nullable=True),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sim',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imsi', sa.String(), nullable=True),
    sa.Column('caller_id_number', sa.String(), nullable=True),
    sa.Column('iccid', sa.String(), nullable=True),
    sa.Column('network_operator', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sim')
    op.drop_table('patient')
    op.drop_table('device')
    ### end Alembic commands ###
