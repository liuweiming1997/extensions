"""add_table_douban_dianying

Revision ID: 8da75faa68a8
Revises: 6f2e099ed288
Create Date: 2019-03-19 16:38:08.259951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8da75faa68a8'
down_revision = '6f2e099ed288'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'douban_dianying',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('score', sa.Float(10, 2), nullable=False),
        sa.Column('region', sa.String(200), nullable=False),
        sa.Column('img', sa.String(200), nullable=False),
        sa.Column('url', sa.String(200), nullable=False),
        sa.Column('buy_ticket', sa.String(200), nullable=False),
        sa.Column('create_time', mysql.TIMESTAMP(), autoincrement=False, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('douban_dianying')
