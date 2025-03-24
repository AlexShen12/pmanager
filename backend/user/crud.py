# external
from sqlalchemy.orm import Session

# internal
from .models import User, Credential
from .schemas import UserCreate, UserUpdate, CredentialCreate, CredentialUpdate


def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(
        email=user.email,
        username=user.username,
        password=user.password,  # remeber to implement hash later on.
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_email: str) -> User | None:
    return db.query(User).where(User.user_email == user_email).first()


def update_user(
    db: Session, user_update: UserUpdate, user_id: int) -> User:  # really neeed to remember implementing hashing
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    update_data = user_update.model_dump(exclude_unset = True, by_alias = True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).where(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    db.refresh(db_user)
    return


def create_cred(db: Session, cred: CredentialCreate) -> Credential:
    db_cred = Credential(
        website=cred.website, subusername=cred.subusername, subpassword=cred.subpassword
    )
    db.add(db_cred)
    db.commit()
    db.refresh()
    return db_cred


def get_cred(db: Session, cred_user: str) -> Credential | None:
    return db.query(Credential).where(Credential.subusername == cred_user).first()

def update_cred(db: Session, cred_u: str, cred_update: CredentialUpdate) -> Credential:
    db_cred = get_cred(db, cred_u)
    if db_cred is None:
        return None
    update_data = cred_update.model_dump(exclude_unset=True, by_alias=True)
    for name, value in update_data:
        setattr(db_cred, name, value)
    db.commit()
    db.refresh(db_cred)
    return db_cred


def delete_cred(db: Session, cred_id: int):
    db_cred = db.query(Credential).where(Credential.id == cred_id).first()
    db.delete(db_cred)
    db.commit()
    db.refresh(db_cred)
    return
