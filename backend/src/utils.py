# utils.py
from passlib.context import CryptContext
from cryptography.fernet import Fernet
from src.globals.config import Settings  # Adjust the import as per your project structure

settings = Settings()

# Initialize cipher with key from settings
cipher_suite = Fernet(settings.FERNgET_KEY.encode())

# Context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()