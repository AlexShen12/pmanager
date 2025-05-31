
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.tests.testutils import random_email, random_lower_string
from user.models import User, Credential


def create_random_user(db: Session) -> User:
    email = random_email()
    username = random_lower_string(8)
    password = f"{random_lower_string(8)}@#123!"
    user = User(
        user_email=email,
        username=username,
        password=password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_random_credential(db: Session, user_id: int = None) -> Credential:
    if user_id is None:
        user = create_random_user(db)
        user_id = user.id

    website = random_lower_string(10)
    subusername = random_lower_string(10)
    subpassword = f"{random_lower_string(10)}@#123!"
    cred = Credential(
        website=website,
        subusername=subusername,
        subpassword=subpassword,
        user_id=user_id,
    )
    db.add(cred)
    db.commit()
    db.refresh(cred)
    return cred

# User Tests

def test_create_user(client: TestClient):
    """Test user creation endpoint"""
    user_data = {
        "id": 1,
        "user_email": "hellotesting@gmail.com",
        "username": "testingusername",
        "password": "testingpassword@#123!",
    }
    response = client.post("/user/signup/", json=user_data)





