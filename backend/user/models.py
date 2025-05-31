# external
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, mapped_column, Mapped, validates

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    user_email: Mapped[str] = mapped_column(String, unique = True)
    username: Mapped[str]
    password: Mapped[str]

    # Password length validation is handled in utils.py before hashing
    # No database constraints needed for hashed passwords

    @validates('user_email')
    def validate_email(self, _key, address):
        if "@" not in address:
            raise ValueError("Valid email address required.")
        return address

    # Password validation is handled in utils.py before hashing
    # No validation needed here since we store hashed passwords

    credentials: Mapped[list["Credential"]] = relationship(
        "Credential",
        back_populates= "user",
        cascade = "all, delete-orphan"
    )

class Credential(Base):
    __tablename__ = "Credentials"
    id: Mapped[int] = mapped_column(Integer, primary_key = True, index = True)
    website: Mapped[str] = mapped_column(String, index = True)
    subusername: Mapped[str]
    subpassword: Mapped[str]

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('User.id'))

    user: Mapped[list["User"]] = relationship(
        "User",
        back_populates="credentials"
    )




#Nullable or deffered look into
