"""version1

Revision ID: 586e6fc3fd99
Revises: 
Create Date: 2022-06-24 12:06:05.659549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '586e6fc3fd99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('clase', sa.String(), nullable=True),
    sa.Column('evolucion', sa.String(), nullable=True),
    sa.Column('ataque_estrella', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
