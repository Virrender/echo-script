from sqlalchemy import (
    Integer, 
    String, 
    Column, 
    Text, 
    DateTime,
    func
    )

from .database import Base


class Recordings(Base):
    __tablename__ = "recordings"
    id = Column(
        Integer,
        primary_key=True
    )
    created_at = Column(DateTime(timezone=True), nullable=False)
    audio_path = Column(String, nullable=False)
    transcript = Column(Text, nullable=True)


class Users(Base):
    __tablename__= "users"

    id=Column(
        Integer,
        primary_key=True
    )
    username=Column(String, nullable=False)
    hashed_password=Column(String, nullable=False)
    created_at=Column(
        DateTime(timezone=True),
        server_default=func.now()
        )

    updated_at=Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
