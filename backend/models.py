from sqlalchemy import Column, Integer, String, Numeric
from database import Base


class Item(Base):
    __tablename__ = "items"

    # primary_key=True automatically makes this column auto-increment in SQLite
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
    password = Column(String, nullable=False)
