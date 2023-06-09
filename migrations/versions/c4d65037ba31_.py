"""empty message

Revision ID: c4d65037ba31
Revises: 144cb4a84248
Create Date: 2023-06-04 16:54:57.256634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4d65037ba31'
down_revision = '144cb4a84248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seat_num', sa.String(length=50), nullable=True))
        batch_op.drop_column('seat')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seat', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('seat_num')

    # ### end Alembic commands ###
