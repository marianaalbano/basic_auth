"""empty message

Revision ID: cccc25102623
Revises: 
Create Date: 2018-02-01 20:45:58.501663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cccc25102623'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('senha', sa.String(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sobrenome', sa.String(), nullable=False),
    sa.Column('data_login', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuarios')
    # ### end Alembic commands ###
