"""Update Comments tables

Revision ID: 6f4b340f9f7a
Revises: f05a5d5bcf6b
Create Date: 2019-10-28 15:45:53.301958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4b340f9f7a'
down_revision = 'f05a5d5bcf6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=10000), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('blogs', sa.Column('comments_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'comments', ['comments_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'comments_id')
    op.drop_table('comments')
    # ### end Alembic commands ###