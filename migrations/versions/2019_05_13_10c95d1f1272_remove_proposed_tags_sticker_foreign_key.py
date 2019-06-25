"""Remove proposed tags sticker foreign key

Revision ID: 10c95d1f1272
Revises: a80fa524a2ba
Create Date: 2019-05-13 19:30:57.615293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10c95d1f1272'
down_revision = 'a80fa524a2ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('proposed_tags_sticker_file_id_fkey', 'proposed_tags', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('proposed_tags_sticker_file_id_fkey', 'proposed_tags', 'sticker', ['sticker_file_id'], ['file_id'])
    # ### end Alembic commands ###