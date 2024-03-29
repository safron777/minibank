"""Initial migration Account email fk

Revision ID: fd47c512aefe
Revises: 260c32eef41d
Create Date: 2024-03-10 22:00:51.030535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd47c512aefe'
down_revision: Union[str, None] = '260c32eef41d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_accounts_id_fkey', 'user_accounts', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'users', ['email'], ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('user_accounts_id_fkey', 'user_accounts', 'users', ['id'], ['id'])
    # ### end Alembic commands ###
