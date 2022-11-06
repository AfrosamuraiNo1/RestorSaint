"""Initial migration.

Revision ID: 102b642b3621
Revises: 
Create Date: 2022-10-30 23:00:23.381762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102b642b3621'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('place')
    # ### end Alembic commands ###