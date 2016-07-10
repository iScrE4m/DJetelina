"""empty message

Revision ID: e7fa899d5912
Revises: 54b962ccf660
Create Date: 2016-07-10 02:03:37.846881

"""

# revision identifiers, used by Alembic.
revision = 'e7fa899d5912'
down_revision = '54b962ccf660'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['email'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    ### end Alembic commands ###