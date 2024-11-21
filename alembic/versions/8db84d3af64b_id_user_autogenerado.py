"""Id user autogenerado

Revision ID: 8db84d3af64b
Revises: 8d1f28034653
Create Date: 2024-11-21 13:36:07.912415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8db84d3af64b'
down_revision: Union[str, None] = '8d1f28034653'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
