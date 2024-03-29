"""empty message

Revision ID: 079a2bd011d6
Revises: 6523027a0c57
Create Date: 2024-03-07 00:27:57.219804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '079a2bd011d6'
down_revision = '6523027a0c57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('posted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='posts_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='posts_pkey')
    )
    op.drop_table('post')
    # ### end Alembic commands ###
