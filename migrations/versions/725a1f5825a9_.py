"""empty message

Revision ID: 725a1f5825a9
Revises: 4084cb814fa0
Create Date: 2017-08-06 22:28:55.651312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725a1f5825a9'
down_revision = '4084cb814fa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('firstname', sa.String(length=40), nullable=True))
    op.add_column('user', sa.Column('lastname', sa.String(length=40), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    # ### end Alembic commands ###
