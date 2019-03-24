"""add_table_medium_programming

Revision ID: fa585dc534f5
Revises: 1680383f4bc4
Create Date: 2019-03-24 23:01:05.833361

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fa585dc534f5'
down_revision = '1680383f4bc4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'medium_programming',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
        sa.Column('hash_id', sa.Integer(), autoincrement=False, nullable=False),
        sa.Column('title', sa.String(200), autoincrement=False, nullable=False),
        sa.Column('url', sa.String(2000), autoincrement=False, nullable=False), 
        sa.Column('create_time', mysql.TIMESTAMP(), autoincrement=False, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('medium_programming')
