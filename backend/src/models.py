from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    #pwlist = Column(JSON) # Need to figure out how to validate before storing as well... Can do as dict since serialization is automatic

    # linkes to stored credentials
    credentials = relationship("Credential", back_populates= "owner", cascade= "all, delete orphan")


class Credential(Base):
    __tablename__ = "credentials"

    id = Column(Integer, primary_key= True, index = True)
    website = Column(String, index = True)
    login = Column(String)
    enc_pass = Column(String)

    # To link back to user who owns this sheet. 

    owner_id = Column(Integer, ForeignKey('users.id'), nullable= False)
    owner = relationship("User", back_populates="credentials")

# might need to use backref? Still thinking about it.
# Potentially can allow users to categorize passwords under different categories. 
    
# Is it safe to store data like this? Access to main username gives access to all... 
    