"""Fix change check task delete cascade

Revision ID: 9503a8aea135
Revises: 10c95d1f1272
Create Date: 2019-05-20 19:16:31.376620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9503a8aea135'
down_revision = '10c95d1f1272'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('change_check_task_id_fkey', 'change', type_='foreignkey')
    op.create_foreign_key(None, 'change', 'task', ['check_task_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'change', type_='foreignkey')
    op.create_foreign_key('change_check_task_id_fkey', 'change', 'task', ['check_task_id'], ['id'])
    # ### end Alembic commands ###
