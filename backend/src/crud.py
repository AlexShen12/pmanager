from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate
# from app.security import hash_password, verify_password  # Assume you have these functions

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
