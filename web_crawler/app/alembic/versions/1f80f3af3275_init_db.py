"""init db

Revision ID: 1f80f3af3275
Revises: 
Create Date: 2019-03-16 14:31:28.755162

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f80f3af3275'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(200), autoincrement=True, nullable=False),
        sa.Column('password', sa.String(200), autoincrement=True, nullable=False),
        sa.Column('create_time', mysql.TIMESTAMP(), autoincrement=False, nullable=True, server_default=sa.text('CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('user')
