# external
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

# internal
from user import crud, schemas
from src.db import get_db

cred_router: APIRouter = APIRouter(prefix = "/credentials")

@cred_router.post("/create", response_class = schemas.CredentialResponse)
def create_cred(new_cred: schemas.CredentialCreate, db: Session = Depends(get_db)):
    new_cred = crud.create_cred(db, new_cred)
    # need to encrypt 
    return new_cred

@cred_router.get("/overview", response_class= schemas.CredentialResponse)
def get_cred(cred: schemas.CredentialResponse, db: Session = Depends(get_db)):
    get_cred = crud.get_cred(db, cred) # why is it a user id need to update
    return get_cred

@cred_router.put("/credupdate", response_model= schemas.CredentialResponse)
def update_cred(cred_u: schemas.CredentialUpdate, db: Session = Depends(get_db)):
    #have to somehow get this from the db and I have no idea if it does it automatically. 
    update_user = crud.update_cred(db,cred_update = cred_u)
    return update_user

@cred_router.delete("/delete/", response_model = schemas.DelResponse) 
# how do websites get this on the same page as update user 
def delete_cred(user_u: schemas.UserBase, db: Session = Depends(get_db)):
    if not user_u:
        raise HTTPException(status_code = 400, detail = "Unable to delete user.")
    del_user = crud.delete_user(db, user_u.id)
    return del_user
