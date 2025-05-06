from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime, timezone

class Itemdb(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)  
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    name = Column(String)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    address_postal_code = Column(String)
    address_city = Column(String)
    profile_first_name = Column(String)
    profile_last_name = Column(String)
    company_name = Column(String)
