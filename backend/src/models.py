# built-in
import re

# external
from sqlalchemy import Integer, String, ForeignKey 
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped, validates
from sqlalchemy.schema import CheckConstraint

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    email: Mapped[str] = mapped_column(String, unique = True)
    username: Mapped[str] 
    password: Mapped[str] 

    __table_args__ = (
        CheckConstraint(
        'char_length(password) > 10', 
        name = 'p_length_check'),
    )
    
    @validates('email')
    def validate_email(self, key, address):
        if "@" not in address:
            raise ValueError("Valid email address required.")
        return address
    
    @validates('password')
    def validate_password(self, key, password):
        if not len(password) >= 10:
            raise ValueError("Password Length must be at least 10 characters.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValueError("Password must contain at least one special character.")
        return password
    
    credentials: Mapped[list["Credential"]] = relationship(
        "Credential",
        back_populates= "user",
        cascade = "all, delete-orphan"
    )

class Credential(Base):
    __tablename__ = "Credentials"
    id: Mapped[int] = mapped_column(Integer, primary_key =True, index = True)
    website: Mapped[str] = mapped_column(String, index = True)
    subusername: Mapped[str]
    subpassword: Mapped[str]

    user_id = Mapped[int] = mapped_column(Integer, ForeignKey('User.id'))

    user: Mapped[list["User"]] = relationship(
        "User",
        back_populates="credentials"
    )




#Nullable or deffered look into 
