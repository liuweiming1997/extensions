"""meituan_meishi

Revision ID: 2d0977543bf6
Revises: 1f80f3af3275
Create Date: 2019-03-16 15:05:29.331994

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2d0977543bf6'
down_revision = '1f80f3af3275'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'meituan_meishi',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, primary_key=True),
        sa.Column('poiId', sa.Integer(), nullable=False),
        sa.Column('frontImg', sa.String(200), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('avgScore', sa.Float(10, 2), nullable=False),
        sa.Column('allCommentNum', sa.Integer(), nullable=False),
        sa.Column('address', sa.String(200), nullable=False),
        sa.Column('avgPrice', sa.Float(10, 2), nullable=False),
        sa.Column('create_time', mysql.TIMESTAMP(), autoincrement=False, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('meituan_meishi')
