"""Añadir rol al usuario

Revision ID: ae1bc017c8cf
Revises: eba014b4610a
Create Date: 2024-11-21 12:03:21.017893

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae1bc017c8cf'
down_revision: Union[str, None] = 'eba014b4610a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('cliente', sa.Column('rol', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('cliente', 'rol')
