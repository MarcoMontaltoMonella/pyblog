"""new fields in user model

Revision ID: 069edc868f93
Revises: d34f2f8376c5
Create Date: 2018-08-23 14:54:09.506145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '069edc868f93'
down_revision = 'd34f2f8376c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
