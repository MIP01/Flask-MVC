"""empty message

Revision ID: 4350070fd665
Revises: a5f332c919d0
Create Date: 2022-07-25 19:23:37.606583

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4350070fd665'
down_revision = 'a5f332c919d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('inserttable')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inserttable',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('password', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('write_api', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('read_api', mysql.VARCHAR(length=32), nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
