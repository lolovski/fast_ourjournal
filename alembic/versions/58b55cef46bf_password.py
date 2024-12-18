"""password

Revision ID: 58b55cef46bf
Revises: 5b209da27d5c
Create Date: 2024-08-12 12:25:45.558715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '58b55cef46bf'
down_revision: Union[str, None] = '5b209da27d5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###
