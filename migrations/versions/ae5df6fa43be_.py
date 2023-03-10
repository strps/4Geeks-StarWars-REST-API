"""empty message

Revision ID: ae5df6fa43be
Revises: 59c641f655b1
Create Date: 2023-02-01 16:41:32.068248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae5df6fa43be'
down_revision = '59c641f655b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('created_by_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('created_by_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
