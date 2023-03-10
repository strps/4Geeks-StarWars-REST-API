"""empty message

Revision ID: dca6dc7c1047
Revises: c7b56687373b
Create Date: 2023-02-01 19:27:27.258287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dca6dc7c1047'
down_revision = 'c7b56687373b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint('character_homeworld_id_fkey', type_='foreignkey')
        batch_op.drop_column('homeworld_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeworld_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('character_homeworld_id_fkey', 'planet', ['homeworld_id'], ['id'])

    # ### end Alembic commands ###
