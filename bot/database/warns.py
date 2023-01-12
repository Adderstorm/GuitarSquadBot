import sqlalchemy as sa
from .BaseModel import BaseModel

import datetime

class Warns(BaseModel):
    __tablename__ = 'warns'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    server_id = sa.Column(sa.Integer, nullable=False)
    moderator_id = sa.Column(sa.Integer, nullable=False)
    reason = sa.Column(sa.String(255), nullable=False)
    created_at = sa.Column(sa.DATETIME, nullable=False, server_default=sa.func.now())

    def __init__(self, user_id, server_id, moderator_id, reason, created_at) -> None:
        self.user_id = user_id
        self.server_id = server_id
        self.moderator_id = moderator_id
        self.reason = reason
        self.created_at = created_at