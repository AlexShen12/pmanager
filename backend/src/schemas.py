from pydantic import BaseModel, ConfigDict
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

class CredentialBase(BaseModel): 
    platform: str
    login: str

class CredentialCreate(CredentialBase):
    password: str  

class CredentialUpdate(BaseModel):
    platform: str | None = None
    login: str | None = None
    password: str | None = None

class Credential(CredentialBase):
    id: int
    owner_id: int
    model_config:ConfigDict = ConfigDict(from_attributes= True)

class User(UserBase):
    id: int
    credentials: List[Credential] = []
    model_config:ConfigDict = ConfigDict(from_attributes= True)


        