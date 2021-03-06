"""followers

Revision ID: 1739fdc6dab4
Revises: 331624f0f975
Create Date: 2018-11-14 10:09:09.384253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1739fdc6dab4'
down_revision = '331624f0f975'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
