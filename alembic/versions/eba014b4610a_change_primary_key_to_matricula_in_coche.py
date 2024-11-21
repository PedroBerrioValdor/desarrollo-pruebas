"""Change primary key to matricula in coche

Revision ID: eba014b4610a
Revises: 
Create Date: 2024-11-19 10:56:50.426862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eba014b4610a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'coche_new',
        sa.Column('matricula', sa.String(), nullable=False),
        sa.Column('marca', sa.String(), nullable=True),
        sa.Column('tipoAveria', sa.String(), nullable=True),
        sa.Column('idCliente', sa.Integer(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['idCliente'], ['cliente.id'], ),
        sa.PrimaryKeyConstraint('matricula')
    )
    
    # 2. Copiar los datos de la tabla original 'coche' a 'coche_new'
    op.execute('INSERT INTO coche_new (matricula, marca, tipoAveria, idCliente, updated_at, created_at, active) SELECT id, marca, tipoAveria, idCliente, updated_at, created_at, active FROM coche')
    
    # 3. Eliminar la tabla original
    op.drop_table('coche')

    # 4. Renombrar 'coche_new' a 'coche'
    op.rename_table('coche_new', 'coche')


def downgrade() -> None:
    pass
