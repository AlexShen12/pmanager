# external
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

# internal
from user import crud, schemas
from src.db import get_db

cred_router: APIRouter = APIRouter(prefix = "/credentials")

# general refactoring of CRUD and schemas needed.

@cred_router.post("/create", response_model = schemas.CredentialResponse) # want to update with async later on.
def create_cred(new_cred: schemas.CredentialCreate, user_id: int, db: Session = Depends(get_db)):
    # Encryption is now handled in the CRUD function
    created_cred = crud.create_cred(db, new_cred, user_id)
    return created_cred

@cred_router.get("/user/{user_id}", response_model=list[schemas.CredentialResponse])
def get_user_credentials(user_id: int, db: Session = Depends(get_db)):
    """Get all credentials for a specific user (encrypted passwords not returned)."""
    credentials = crud.get_user_credentials(db, user_id)
    return credentials

@cred_router.get("/decrypt/{cred_id}")
def get_credential_decrypted(cred_id: int, db: Session = Depends(get_db)):
    """Get a specific credential with decrypted password."""
    credential = crud.get_credential_with_decrypted_password(db, cred_id)
    if not credential:
        raise HTTPException(status_code=404, detail="Credential not found")
    return credential

@cred_router.put("/update/{cred_id}", response_model=schemas.CredentialResponse)
def update_cred(cred_id: int, cred_update: schemas.CredentialUpdate, db: Session = Depends(get_db)):
    """Update a credential. Password will be encrypted if provided."""
    updated_cred = crud.update_cred(db, cred_id, cred_update)
    if not updated_cred:
        raise HTTPException(status_code=404, detail="Credential not found")
    return updated_cred

@cred_router.delete("/delete/{cred_id}", response_model=schemas.DelResponse)
def delete_cred(cred_id: int, db: Session = Depends(get_db)):
    """Delete a specific credential."""
    success = crud.delete_cred(db, cred_id)
    if not success:
        raise HTTPException(status_code=404, detail="Credential not found")
    return schemas.DelResponse(detail="Credential deleted successfully.")
