"""empty message

Revision ID: 38bf7ab202a6
Revises: 25d77ee74059
Create Date: 2024-03-03 12:14:36.475276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38bf7ab202a6'
down_revision = '25d77ee74059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=20),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###
