"""Initial migration Balance

Revision ID: ac76bb148f59
Revises: 81f9cb9e86d1
Create Date: 2024-03-09 22:36:34.845641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac76bb148f59'
down_revision: Union[str, None] = '81f9cb9e86d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_accounts', 'accounts',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.drop_column('user_accounts', 'interest_rate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_accounts', sa.Column('interest_rate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.alter_column('user_accounts', 'accounts',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
