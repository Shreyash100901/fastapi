"""Create owner_id col on todos table

Revision ID: 35d3e2c46e92
Revises: 53ea260b5f91
Create Date: 2024-06-30 11:27:46.137628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35d3e2c46e92'
down_revision: Union[str, None] = '53ea260b5f91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('todos',sa.Column('owner_id',sa.Integer(), nullable=True))


def downgrade() -> None:
    pass
