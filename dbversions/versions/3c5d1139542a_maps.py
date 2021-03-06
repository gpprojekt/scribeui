"""maps

Revision ID: 3c5d1139542a
Revises: 4e158a994bb7
Create Date: 2014-01-22 15:44:54.003005

"""

# revision identifiers, used by Alembic.
revision = '3c5d1139542a'
down_revision = '4e158a994bb7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=30), nullable=False),
    sa.Column('type', sa.Unicode(length=30), nullable=False),
    sa.Column('description', sa.Unicode()),
    sa.Column('projection', sa.Unicode()),
    sa.Column('extent', sa.Unicode(50)),
    sa.Column('git_url', sa.Unicode()),
    sa.Column('workspace_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id']),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maps')
    ### end Alembic commands ###
