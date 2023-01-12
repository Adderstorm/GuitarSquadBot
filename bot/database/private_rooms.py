import sqlalchemy as sa

from .BaseModel import BaseModel

class PrivateRooms(BaseModel):
    __tablename__ = 'private_rooms'

    id = sa.Column(sa.Integer, nullable=False, primary_key=True, autoincrement=True)
    server_id = sa.Column(sa.Integer, nullable=False)
    category_id = sa.Column(sa.Integer, nullable=False)
    channel_id = sa.Column(sa.Integer, nullable = False)

    def __init__(self, server_id, category_id, channel_id) -> None:
        self.server_id = server_id
        self.category_id = category_id
        self.channel_id = channel_id