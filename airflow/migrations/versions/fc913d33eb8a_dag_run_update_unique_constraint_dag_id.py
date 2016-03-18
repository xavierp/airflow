"""dag_run update unique constraint dag_id

Revision ID: fc913d33eb8a
Revises: cd63bfc56b5e
Create Date: 2016-03-18 18:42:12.244021

"""

# revision identifiers, used by Alembic.
revision = 'fc913d33eb8a'
down_revision = 'cd63bfc56b5e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_constraint('dag_id', 'dag_run')
    op.create_unique_constraint('dag_id', 'dag_run', ['dag_id', 'execution_date', 'conf_hash'])


def downgrade():
    op.drop_constraint('dag_id', 'dag_run')
    op.create_unique_constraint('dag_id', 'dag_run', ['dag_id', 'execution_date'])
