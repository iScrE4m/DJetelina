"""empty message

Revision ID: a46258bbaf10
Revises: cad4b861c6f3
Create Date: 2016-07-10 02:14:38.759377

"""

# revision identifiers, used by Alembic.
revision = 'a46258bbaf10'
down_revision = '54b962ccf660'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hash', sa.String(length=300), nullable=True))
    op.create_unique_constraint(None, 'user', ['email'])
    op.drop_column('user', 'password')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'hash')
    ### end Alembic commands ###
