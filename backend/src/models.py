from sqlalchemy import Column, Integer, String, JSON
from src.database.db import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    pwlist = Column(JSON) # Need to figure out how to validate before storing as well... Can do as dict since serialization is automatic


# Is it safe to store data like this? Access to main username gives access to all... 
    