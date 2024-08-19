"""first name

Revision ID: c35d26d3d673
Revises: 301d0f9d1dda
Create Date: 2024-08-12 14:41:22.638855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c35d26d3d673'
down_revision: Union[str, None] = '301d0f9d1dda'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=False))
    op.drop_column('user', 'firs_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firs_name', sa.VARCHAR(length=64), nullable=False))
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###
