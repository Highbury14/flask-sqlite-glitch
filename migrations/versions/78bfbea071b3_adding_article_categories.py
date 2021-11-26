"""Adding article categories

Revision ID: 78bfbea071b3
Revises: afff4cf5a96b
Create Date: 2021-11-11 01:44:58.726510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78bfbea071b3'
down_revision = 'afff4cf5a96b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('category_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('slug', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('category_id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('article_categories',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.article_id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.category_id'], ),
    sa.PrimaryKeyConstraint('article_id', 'category_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_categories')
    op.drop_table('category')
    # ### end Alembic commands ###
