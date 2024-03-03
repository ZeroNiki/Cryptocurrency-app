"""second init

Revision ID: 6b3d05ed5a27
Revises: e8eaa2021764
Create Date: 2024-02-24 17:11:19.218507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b3d05ed5a27'
down_revision: Union[str, None] = 'e8eaa2021764'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
