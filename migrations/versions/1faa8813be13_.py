"""empty message

Revision ID: 1faa8813be13
Revises: 495400dca346
Create Date: 2023-05-29 01:52:51.154554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1faa8813be13'
down_revision = '495400dca346'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t__user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('line_id', sa.String(length=50), nullable=True),
    sa.Column('display_name', sa.String(length=255), nullable=True),
    sa.Column('picturl_url', sa.String(length=255), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('line_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t__user')
    # ### end Alembic commands ###