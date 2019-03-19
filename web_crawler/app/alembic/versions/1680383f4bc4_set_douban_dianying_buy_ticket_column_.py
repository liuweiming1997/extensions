"""set_douban_dianying_buy_ticket_column_can_null

Revision ID: 1680383f4bc4
Revises: 2e04554c3d2b
Create Date: 2019-03-19 22:04:25.354555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1680383f4bc4'
down_revision = '2e04554c3d2b'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('douban_dianying', 'buy_ticket', existing_type=sa.String(2000), nullable=True)


def downgrade():
    op.alter_column('douban_dianying', 'buy_ticket', existing_type=sa.String(2000), nullable=False)
