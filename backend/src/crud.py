from sqlalchemy.orm import Session
from src.models import User, Credential
from src.schemas import UserCreate, UserUpdate, CredentialCreate, CredentialUpdate

# from app.security import hash_password, verify_password  # Assume you have these functions

# remember ot move to main out of SRC no need for SRC ATP idk even fucj
# Create a new user
def create_user(db: Session, user: UserCreate):
    hashed_password = user.password #Hopefully hashed later.
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get all users Not sure when this would be useful but im all here for it. 
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# Update a user
def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user_update.username:
            db_user.username = user_update.username
        if user_update.email:
            db_user.email = user_update.email
        if user_update.password:
            db_user.password = user_update.password #remember to hash
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

'''Credential CRUD'''

#creates a new credential 
def create_credential(db: Session, credential: CredentialCreate, user_id:int):
    encrypted_pw = encrypt_pw() # need to encrypt!!
    db_credential = Credential(platform = credential.platform, login = credential.login, password = encrypted_pw)
    db.add(db_credential)
    db.commit()
    db.refresh(db_credential)
    return db_credential

#finds a credential for the user
def get_credential(db: Session, credential_id: int): 
    return db.query(Credential).filter(Credential.id == credential_id).first()

# Get all credential under a user.
def get_users(db: Session, skip: int = 0, limit: int = 10 ): #limit is lowkey low maybe make it higher.
    return db.query(Credential).offset(skip).limit(limit).all()
# copy pasted might need to edit later. 

# Update a user
def update_credential(db: Session, credential_id: int, credential_update: CredentialUpdate):
    db_user = db.query(Credential).filter(Credential.id == credential_id).first()
    if db_user:
        if credential_update.platform:
            db_user.platform = credential_update.platform
        if credential_update.login:
            db_user.email = credential_update.email
        if credential_update.password:
            db_user.password = credential_update.password #remember to hash
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# Delete a user
def delete_credential(db: Session, credential_id: int):
    db_user = db.query(Credential).filter(Credential.id == credential_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None




