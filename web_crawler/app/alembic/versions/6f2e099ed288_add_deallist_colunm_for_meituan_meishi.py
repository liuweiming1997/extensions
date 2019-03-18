"""add_dealList_colunm_for_meituan_meishi

Revision ID: 6f2e099ed288
Revises: 2d0977543bf6
Create Date: 2019-03-18 20:39:09.930912

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f2e099ed288'
down_revision = '2d0977543bf6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('meituan_meishi', sa.Column('dealList', mysql.JSON(), nullable=True, server_default=None))


def downgrade():
    op.drop_column('meituan_meishi', 'dealList')
