#!/usr/bin/env python3
"""
Test script to verify the security functions work correctly.
This script tests password hashing, verification, and credential encryption/decryption.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from user.utils import (
    hash_password,
    verify_password,
    encrypt_credential,
    decrypt_credential,
    validate_password_strength,
    generate_secure_token
)

def test_password_validation():
    """Test password strength validation."""
    print("Testing password validation...")

    # Test weak passwords
    weak_passwords = [
        "short",  # Too short
        "nouppercase123!",  # No uppercase
        "NOLOWERCASE123!",  # No lowercase
        "NoNumbers!",  # No numbers
        "NoSpecialChars123",  # No special characters
    ]

    for password in weak_passwords:
        is_valid, error = validate_password_strength(password)
        print(f"Password '{password}': {'VALID' if is_valid else 'INVALID'} - {error}")
        assert not is_valid, f"Password '{password}' should be invalid"

    # Test strong password
    strong_password = "StrongPassword123!"
    is_valid, error = validate_password_strength(strong_password)
    print(f"Password '{strong_password}': {'VALID' if is_valid else 'INVALID'} - {error}")
    assert is_valid, f"Password '{strong_password}' should be valid"

    print("Password validation tests passed!\n")

def test_password_hashing():
    """Test password hashing and verification."""
    print("Testing password hashing and verification...")

    password = "TestPassword123!"

    # Test hashing
    hashed = hash_password(password)
    print(f"Original password: {password}")
    print(f"Hashed password: {hashed}")

    # Test verification with correct password
    is_valid = verify_password(password, hashed)
    print(f"Verification with correct password: {'PASS' if is_valid else 'FAIL'}")
    assert is_valid, "Password verification should succeed with correct password"

    # Test verification with incorrect password
    wrong_password = "WrongPassword123!"
    is_valid = verify_password(wrong_password, hashed)
    print(f"Verification with wrong password: {'FAIL' if not is_valid else 'PASS'}")
    assert not is_valid, "Password verification should fail with wrong password"

    print("Password hashing tests passed!\n")

def test_credential_encryption():
    """Test credential encryption and decryption."""
    print("Testing credential encryption and decryption...")

    credential = "MySecretPassword123!"

    # Test encryption
    encrypted = encrypt_credential(credential)
    print(f"Original credential: {credential}")
    print(f"Encrypted credential: {encrypted}")

    # Test decryption
    decrypted = decrypt_credential(encrypted)
    print(f"Decrypted credential: {decrypted}")

    # Verify they match
    assert credential == decrypted, "Decrypted credential should match original"
    print("Credential encryption tests passed!\n")

def test_token_generation():
    """Test secure token generation."""
    print("Testing secure token generation...")

    token1 = generate_secure_token()
    token2 = generate_secure_token()

    print(f"Token 1: {token1}")
    print(f"Token 2: {token2}")

    # Tokens should be different
    assert token1 != token2, "Generated tokens should be unique"

    # Tokens should be the expected length (32 bytes = 64 hex characters)
    assert len(token1) == 64, "Token should be 64 characters long"
    assert len(token2) == 64, "Token should be 64 characters long"

    print("Token generation tests passed!\n")

def test_edge_cases():
    """Test edge cases and error handling."""
    print("Testing edge cases...")

    # Test empty password hashing
    try:
        hash_password("")
        assert False, "Should raise ValueError for empty password"
    except ValueError as e:
        print(f"Empty password correctly rejected: {e}")

    # Test empty credential encryption
    try:
        encrypt_credential("")
        assert False, "Should raise ValueError for empty credential"
    except ValueError as e:
        print(f"Empty credential correctly rejected: {e}")

    # Test invalid decryption
    try:
        decrypt_credential("invalid_encrypted_data")
        assert False, "Should raise ValueError for invalid encrypted data"
    except ValueError as e:
        print(f"Invalid encrypted data correctly rejected: {e}")

    print("Edge case tests passed!\n")

def main():
    """Run all tests."""
    print("Testing Password Manager Security Functions\n")
    print("=" * 50)

    try:
        test_password_validation()
        test_password_hashing()
        test_credential_encryption()
        test_token_generation()
        test_edge_cases()

        print("🎉 All security tests passed successfully!")
        print("Your password manager security implementation is working correctly.")

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
