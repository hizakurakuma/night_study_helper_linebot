"""empty message

Revision ID: 1bb29e89e679
Revises: eedc91d543e2
Create Date: 2023-06-04 17:21:31.407800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bb29e89e679'
down_revision = 'eedc91d543e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reserv_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('reserv_count')

    # ### end Alembic commands ###
