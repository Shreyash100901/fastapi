"""Create phone number for users column

Revision ID: 53ea260b5f91
Revises: 
Create Date: 2024-06-30 08:33:14.266734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53ea260b5f91'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(), nullable=True))


def downgrade() -> None:
    pass