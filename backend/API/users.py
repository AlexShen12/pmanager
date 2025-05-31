
# external
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

# internal
from src.db import get_db
from user import crud, schemas

user_router: APIRouter = APIRouter(prefix = "/user")

# Potential security issues too!!!
# general refactoring of CRUD and schemas needed.

@user_router.post("/signup/", response_model= schemas.UserBase)
def make_user(user_cr: schemas.UserCreate, db: Session = Depends(get_db)):
    pot_user = crud.get_user(db, user_cr.email)
    if pot_user:
        raise HTTPException(status_code= 403, detail = "Email is already registered.")
    #need to implement password length checking
    new_user = crud.create_user(db, user_cr)
    return new_user


@user_router.post("/login/", response_model = schemas.UserBase)
def login_user(user_in: schemas.LoginSchema, db: Session = Depends(get_db)):
    # Use the new verify_user_login function that checks password
    authenticated_user = crud.verify_user_login(db, user_in.email, user_in.password)
    if not authenticated_user:
        raise HTTPException(status_code = 401, detail = "Invalid email or password.")
    # would give a token at some point.
    return authenticated_user

@user_router.put("/updateuser/", response_model= schemas.UserBase)
def update_user(user_u: schemas.UserUpdate, db: Session = Depends(get_db)):
    #have to somehow get this from the db and I have no idea if it does it automatically.
    update_user = crud.update_user(db, user_update = user_u, user_id= user_u.id)
    return update_user

@user_router.delete("/delete/", response_model = schemas.DelResponse)
# how do websites get this on the same page as update user
def delete_user(user_u: schemas.UserBase, db: Session = Depends(get_db)):
    if not user_u:
        raise HTTPException(status_code = 400, detail = "Unable to delete user.")
    del_user = crud.delete_user(db, user_u.id)
    return del_user





