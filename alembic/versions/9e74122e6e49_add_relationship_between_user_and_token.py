"""Add relationship between user and token

Revision ID: 9e74122e6e49
Revises: 521225422fa9
Create Date: 2024-06-07 14:04:26.250885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '9e74122e6e49'
down_revision: Union[str, None] = '521225422fa9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tokens', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tokens', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tokens', type_='foreignkey')
    op.drop_column('tokens', 'user_id')
    op.create_table('casbin_rule',
                    sa.Column('id', mysql.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('ptype', mysql.VARCHAR(
                        length=255), nullable=True),
                    sa.Column('v0', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('v1', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('v2', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('v3', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('v4', mysql.VARCHAR(length=255), nullable=True),
                    sa.Column('v5', mysql.VARCHAR(length=255), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    mysql_collate='utf8mb4_0900_ai_ci',
                    mysql_default_charset='utf8mb4',
                    mysql_engine='InnoDB'
                    )
    # ### end Alembic commands ###
