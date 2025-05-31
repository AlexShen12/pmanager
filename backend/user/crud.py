# external
from sqlalchemy.orm import Session
from fastapi import HTTPException

# internal
from .models import User, Credential
from .schemas import UserCreate, UserUpdate, CredentialCreate, CredentialUpdate
from .utils import hash_password, verify_password, encrypt_credential, decrypt_credential


def create_user(db: Session, user: UserCreate) -> User:
    # Hash the password before storing
    try:
        hashed_password = hash_password(user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_user = User(
        user_email=user.email,
        username=user.username,
        password=hashed_password.decode('utf-8'),  # Store as string in database
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_email: str) -> User | None:
    return db.query(User).where(User.user_email == user_email).first()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).where(User.id == user_id).first()


def verify_user_login(db: Session, email: str, password: str) -> User | None:
    """
    Verify user login credentials.

    Args:
        db: Database session
        email: User email
        password: Plain text password

    Returns:
        User object if credentials are valid, None otherwise
    """
    user = get_user(db, email)
    if user and verify_password(password, user.password):
        return user
    return None


def update_user(
    db: Session, user_update: UserUpdate, user_id: int) -> User | None:
    db_user = get_user_by_id(db, user_id)
    if db_user is None:
        return None

    update_data = user_update.model_dump(exclude_unset=True, by_alias=True)

    # Handle password hashing if password is being updated
    if 'password' in update_data:
        try:
            hashed_password = hash_password(update_data['password'])
            update_data['password'] = hashed_password.decode('utf-8')
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    db_user = db.query(User).where(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


def create_cred(db: Session, cred: CredentialCreate, user_id: int) -> Credential:
    # Encrypt the credential password before storing
    try:
        encrypted_password = encrypt_credential(cred.subpassword)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Encryption failed: {str(e)}")

    db_cred = Credential(
        website=cred.website,
        subusername=cred.subusername,
        subpassword=encrypted_password,
        user_id=user_id
    )
    db.add(db_cred)
    db.commit()
    db.refresh(db_cred)
    return db_cred


def get_cred(db: Session, cred_id: int) -> Credential | None:
    return db.query(Credential).where(Credential.id == cred_id).first()


def get_user_credentials(db: Session, user_id: int) -> list[Credential]:
    """Get all credentials for a specific user."""
    return db.query(Credential).where(Credential.user_id == user_id).all()


def get_credential_with_decrypted_password(db: Session, cred_id: int) -> dict | None:
    """Get a credential with its password decrypted."""
    credential = get_cred(db, cred_id)
    if not credential:
        return None

    try:
        decrypted_password = decrypt_credential(credential.subpassword)
        return {
            "id": credential.id,
            "website": credential.website,
            "subusername": credential.subusername,
            "subpassword": decrypted_password,
            "user_id": credential.user_id
        }
    except ValueError:
        # If decryption fails, return None or handle as needed
        return None


def update_cred(db: Session, cred_id: int, cred_update: CredentialUpdate) -> Credential | None:
    db_cred = get_cred(db, cred_id)
    if db_cred is None:
        return None

    update_data = cred_update.model_dump(exclude_unset=True, by_alias=True)

    # Handle password encryption if password is being updated
    if 'subpassword' in update_data and update_data['subpassword']:
        try:
            encrypted_password = encrypt_credential(update_data['subpassword'])
            update_data['subpassword'] = encrypted_password
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Encryption failed: {str(e)}")

    for field, value in update_data.items():
        setattr(db_cred, field, value)

    db.commit()
    db.refresh(db_cred)
    return db_cred


def delete_cred(db: Session, cred_id: int) -> bool:
    db_cred = db.query(Credential).where(Credential.id == cred_id).first()
    if db_cred:
        db.delete(db_cred)
        db.commit()
        return True
    return False
