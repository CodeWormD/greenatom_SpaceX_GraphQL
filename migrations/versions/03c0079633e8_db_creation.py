"""db_creation

Revision ID: 03c0079633e8
Revises: 
Create Date: 2023-02-13 17:31:52.623723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03c0079633e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('launches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mission_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mission_name')
    )
    op.create_index(op.f('ix_launches_id'), 'launches', ['id'], unique=True)
    op.create_table('rockets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_flight', sa.String(length=15), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_rockets_id'), 'rockets', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rockets_id'), table_name='rockets')
    op.drop_table('rockets')
    op.drop_index(op.f('ix_launches_id'), table_name='launches')
    op.drop_table('launches')
    # ### end Alembic commands ###