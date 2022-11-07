from sqlalchemy import Column, Integer, String, TIMESTAMP, text, INT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db', echo=True)

Base = declarative_base()

class blacklist(Base):
    __tablename__ = 'blacklist'

    id = Column(INT, nullable=False, primary_key=True)
    user_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    blacklist = relationship("blacklist")

class private_category(Base):
    __tablename__ = 'private_category'

    id = Column(INT, nullable=False, primary_key=True)
    server_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    channel_id = Column(Integer, nullable = False)
    private_category = relationship("private_category")

class warns(Base):
    __tablename__ = 'warns'

    id = Column(INT, nullable=False, primary_key=True)
    user_id = Column(Integer, nullable=False)
    server_id = Column(Integer, nullable=False)
    moderator_id = Column(Integer, nullable=False)
    reason = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    warns = relationship("warns")

#Base.metadata.create_all(engine)