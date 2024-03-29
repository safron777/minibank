"""Initial migration Balance 4

Revision ID: 78f88efead7c
Revises: e1c6d1566633
Create Date: 2024-03-09 23:31:25.311793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78f88efead7c'
down_revision: Union[str, None] = 'e1c6d1566633'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_accounts', 'interest_rate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_accounts', sa.Column('interest_rate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
