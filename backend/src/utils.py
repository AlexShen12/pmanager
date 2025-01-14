# utils.py
import bcrypt
from cryptography.fernet import Fernet
from src.globals.config import settings  

# Kinda a sketchy way of doing fernet idk 


# Initialize cipher with key from settings
cipher_suite = Fernet(settings.FERNET_KEY)

# Context for password hashing

# Hash a password using bcrypt
def hash_password(password):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password

# Need to hash multiple times 

# Check if the provided password matches the stored password (hashed)
def verify_password(plain_password, hashed_password):
    byte = plain_password.encode('utf-8')
    return bcrypt.checkpw(password = byte , hashed_password = hashed_password)

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

