import sqlalchemy as sa
from .BaseModel import BaseModel

class Blacklist(BaseModel):
    __tablename__ = 'blacklist'

    id = sa.Column(sa.Integer, primary_key=True,nullable=False, autoincrement=True)
    user_id = sa.Column(sa.Integer, nullable=False)
    created_at = sa.Column(sa.DATETIME, server_default=sa.func.now())

    def __init__(self, user_id, created_at) -> None:
        self.user_id = user_id
        self.created_at = created_at