from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base
from datetime import datetime

class ItemDB(Base):
    __tablename__ = "Products"

    createdAt = Column(datetime, default=datetime.now)
    name = Column(String, index=True)
    price = Column(Float)
    description = Column(String)
    color = Column(String)
    stock = Column(Integer)
    id = Column(Integer, primary_key=True, index=True)