import bcrypt
import secrets
import re
from typing import Union

from cryptography.fernet import Fernet, InvalidToken
from src.config import settings

# Initialize cipher with key from settings
try:
    cipher_suite = Fernet(settings.FERNET_KEY)
except Exception as e:
    raise ValueError(f"Invalid Fernet key in settings: {e}")


def validate_password_strength(password: str) -> tuple[bool, str]:

    if len(password) < 10:
        return False, "Password must be at least 10 characters long"

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character"

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"

    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"

    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"

    return True, ""


def hash_password(password: str) -> bytes:
    if not password:
        raise ValueError("Password cannot be empty")

    # Validate password strength before hashing
    is_valid, error_msg = validate_password_strength(password)
    if not is_valid:
        raise ValueError(error_msg)

    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)  
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


def verify_password(plain_password: str, hashed_password: Union[str, bytes]) -> bool:
    if not plain_password or not hashed_password:
        return False

    try:
        # Convert to bytes if it's a string
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode('utf-8')

        plain_bytes = plain_password.encode('utf-8')
        return bcrypt.checkpw(password=plain_bytes, hashed_password=hashed_password)
    except Exception:
        return False


def encrypt_credential(credential: str) -> str:
    if not credential:
        raise ValueError("Credential cannot be empty")

    try:
        encrypted_bytes = cipher_suite.encrypt(credential.encode('utf-8'))
        return encrypted_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Encryption failed: {e}")


def decrypt_credential(encrypted_credential: str) -> str:

    if not encrypted_credential:
        raise ValueError("Encrypted credential cannot be empty")

    try:
        encrypted_bytes = encrypted_credential.encode('utf-8')
        decrypted_bytes = cipher_suite.decrypt(encrypted_bytes)
        return decrypted_bytes.decode('utf-8')
    except InvalidToken:
        raise ValueError("Invalid encrypted credential - decryption failed")
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")


def generate_secure_token(length: int = 32) -> str:
    return secrets.token_hex(length)


# Legacy function names for backward compatibility
def encrypt_password(password: str) -> str:
    return encrypt_credential(password)


def decrypt_password(encrypted_password: str) -> str:
    return decrypt_credential(encrypted_password)



