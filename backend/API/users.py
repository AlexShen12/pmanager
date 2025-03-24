
# external
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

# internal
from src.db import get_db
from user import crud, schemas

user_router: APIRouter = APIRouter()

@user_router.post("/signup/", response_model= schemas.UserBase)
def make_user(user_cr: schemas.UserCreate, db: Session = Depends(get_db)):
    pot_user = crud.get_user(db, user_cr.email)
    if pot_user:
        raise HTTPException(status_code= 403, detail = "Email is already registered.")
    #need to implement password length checking
    new_user = crud.create_user(db, user_cr)
    return new_user


@user_router.get("/login/", response_model = schemas.UserBase)
def login_user(user_in: schemas.LoginSchema, db: Session = Depends(get_db)):
    pot_user = crud.get_user(db, user_email= user_in.email)
    if not pot_user:
        raise HTTPException(status_code = 404, detail = "User does not exist.")
    # would give a token of somepoint at this point.
    return pot_user

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




    
    