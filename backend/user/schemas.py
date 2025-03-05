from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# Potentially use individual BaseModels instead of inheritance for safety?

class CredentialBase(BaseModel):
    website: str 
    subusername: str
    subpassword: str

    model_config: ConfigDict = ConfigDict(
        from_attributes= True, 
        extra= "ignore"
    )

class CredentialCreate(CredentialBase):
    pass

class CredentialResponse(CredentialBase):
    id: int 
    user_id: int 

    model_config: ConfigDict = ConfigDict( 
        from_attributes= True 
    )


class CredentialUpdate(CredentialBase):
    website: Optional[str] = None
    subusername: Optional[str] = None
    subpassword: Optional[str] = None


class UserBase(BaseModel):
    email: EmailStr = Field(..., alias = 'user_email') # unecessary but nice to use/know 
    username: str 
    password: str 

    model_config: ConfigDict = ConfigDict(
        from_attributes= True, 
        extra= "ignore"
    )

class UserCreate(UserBase):
    pass

class UserResponse(UserBase): 
    id: int 
    credentials: list[CredentialResponse] = []

    model_config: ConfigDict = ConfigDict( 
        from_attributes= True 
    )

class UserUpdate(UserBase):
    email: Optional[EmailStr] = Field(None, alias = 'user_email')
    username: Optional[str] = None
    password: Optional[str] = None


