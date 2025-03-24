from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

# Potentially use individual BaseModels instead of inheritance for safety?

class CredentialBase(BaseModel):
    id: int
    website: str 
    subusername: str

    model_config: ConfigDict = ConfigDict(
        from_attributes= True, 
        extra= "ignore"
    )

class CredentialCreate(CredentialBase):
    subpassword: str

class CredentialResponse(CredentialBase):
    id: int 
    user_id: int #???? were you on meth???????

    model_config: ConfigDict = ConfigDict( 
        from_attributes= True 
    )


class CredentialUpdate(CredentialBase):
    website: Optional[str] = None
    subusername: Optional[str] = None
    subpassword: Optional[str] = None


class UserBase(BaseModel):
    id: int
    email: EmailStr = Field(..., alias = 'user_email') # unecessary but nice to use/know 
    username: str 

    model_config: ConfigDict = ConfigDict(
        from_attributes= True, 
        extra= "ignore"
    )

class UserCreate(UserBase):
    password: str 

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

class LoginSchema(BaseModel):
    email: str
    password: str

    model_config: ConfigDict = ConfigDict(
        from_attributes= True
    )

class DelResponse(BaseModel):
    detail: str = "User deleted."
