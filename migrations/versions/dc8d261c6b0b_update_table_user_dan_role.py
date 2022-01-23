"""update table user dan role

Revision ID: dc8d261c6b0b
Revises: 8161832141ad
Create Date: 2022-01-23 14:47:57.898278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc8d261c6b0b'
down_revision = '8161832141ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('about_me', sa.Text(), nullable=True))
    op.add_column('user', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'member_since')
    op.drop_column('user', 'about_me')
    op.drop_column('user', 'location')
    op.drop_column('user', 'name')
    # ### end Alembic commands ###
