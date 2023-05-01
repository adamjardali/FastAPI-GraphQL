"""Second revision

Revision ID: ed65a8d30f56
Revises: 88b5c7c1470d
Create Date: 2023-04-30 14:31:54.731459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed65a8d30f56'
down_revision = '88b5c7c1470d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Users_id', table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('image', sa.VARCHAR(length=100), nullable=True),
    sa.Column('date_of_birth', sa.DATETIME(), nullable=True),
    sa.Column('country', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index('ix_Users_id', 'Users', ['id'], unique=False)
    # ### end Alembic commands ###