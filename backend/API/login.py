
# external
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from backend.user import schemas

#internal
from backend.src.db import get_db
from backend.user import crud

login_router: APIRouter = APIRouter()

# Create a new user
@login_router.post("/signup/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_email(db = db, user_email= user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    return crud.create_user(db=db, user=user)

# Login module -> Get user by ID
@login_router.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Get all users
@login_router.get("/users/", response_model=list[schemas.UserResponse])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

# Update a user
@login_router.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a user
@login_router.delete("/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
