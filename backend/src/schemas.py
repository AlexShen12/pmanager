from pydantic import BaseModel

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


# ???? Model validation makes no sense but tbf have to think about it.
        