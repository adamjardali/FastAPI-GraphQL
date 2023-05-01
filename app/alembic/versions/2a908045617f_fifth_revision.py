"""Fifth revision

Revision ID: 2a908045617f
Revises: 81438f1311ad
Create Date: 2023-04-30 17:38:51.245216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a908045617f'
down_revision = '81438f1311ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Posts_Comments_id', table_name='Posts_Comments')
    op.drop_table('Posts_Comments')
    op.drop_index('ix_Users_id', table_name='Users')
    op.drop_table('Users')
    op.drop_index('ix_Posts_Likes_id', table_name='Posts_Likes')
    op.drop_table('Posts_Likes')
    op.drop_table('Friends')
    op.drop_index('ix_Posts_id', table_name='Posts')
    op.drop_table('Posts')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('written_text', sa.VARCHAR(), nullable=False),
    sa.Column('media_location', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_Posts_id', 'Posts', ['id'], unique=False)
    op.create_table('Friends',
    sa.Column('friend_request', sa.INTEGER(), nullable=False),
    sa.Column('friend_accept', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['friend_accept'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['friend_request'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('friend_request', 'friend_accept')
    )
    op.create_table('Posts_Likes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_Posts_Likes_id', 'Posts_Likes', ['id'], unique=False)
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), nullable=True),
    sa.Column('date_of_birth', sa.DATETIME(), nullable=True),
    sa.Column('country', sa.VARCHAR(length=100), nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), nullable=False),
    sa.Column('is_super_user', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
    op.create_table('Posts_Comments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('comment_text', sa.VARCHAR(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_Posts_Comments_id', 'Posts_Comments', ['id'], unique=False)
    # ### end Alembic commands ###
