"""add_onshow_or_not

Revision ID: 2e04554c3d2b
Revises: 8da75faa68a8
Create Date: 2019-03-19 17:08:32.528341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e04554c3d2b'
down_revision = '8da75faa68a8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('douban_dianying', sa.Column('onshow_time', sa.String(200), nullable=True, server_default=None))

    op.alter_column('douban_dianying', 'url', type_=sa.String(2000))
    op.alter_column('douban_dianying', 'img', type_=sa.String(2000))
    op.alter_column('douban_dianying', 'buy_ticket', type_=sa.String(2000))


def downgrade():
    op.drop_column('douban_dianying', 'onshow_time')

    op.alter_column('douban_dianying', 'url', type_=sa.String(200))
    op.alter_column('douban_dianying', 'img', type_=sa.String(200))
    op.alter_column('douban_dianying', 'buy_ticket', type_=sa.String(200))
