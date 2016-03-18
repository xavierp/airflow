"""dag_run add conf_hash column

Revision ID: cd63bfc56b5e
Revises: 1968acfc09e3
Create Date: 2016-03-18 18:35:03.757813

"""

# revision identifiers, used by Alembic.
revision = 'cd63bfc56b5e'
down_revision = '1968acfc09e3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('dag_run', sa.Column('conf_hash', sa.String(32), nullable=True))


def downgrade():
    op.drop_column('dag_run', 'conf_hash')
