"""empty message

Revision ID: d2e18f0f34a9
Revises: a60315eb2654
Create Date: 2019-10-09 14:07:45.528774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d2e18f0f34a9"
down_revision = "a60315eb2654"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project_favorites",
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("project_favorites")
    # ### end Alembic commands ###