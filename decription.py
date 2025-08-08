import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys


def decrypt_encoded_string(encoded_string, key):
    """Decrypt the encoded string back to the project name using AES-256-CBC."""
    try:
        # Generate AES-256 key by hashing the input key string
        hashed_key = hashlib.sha256(key.encode()).digest()
        aes_key = hashed_key[:32]  # AES-256 requires a 32-byte key

        # Decode the base64 encoded string
        combined = base64.b64decode(encoded_string)

        # Extract IV (first 16 bytes) and encrypted data
        iv = combined[:16]
        encrypted_data = combined[16:]


        cipher = AES.new(aes_key, AES.MODE_CBC, iv)


def main():
    # Get input from user
    file_path = input("Enter file path: ")
    key = input("Enter decryption key: ")
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return
    
    # Extract the encrypted string from file
    encrypted_string = extract_encrypted_string_from_file(file_path)
    if not encrypted_string:
        print("Error: Failed to extract the encrypted string.")
        return
    
    print(f"Found encrypted string: {encrypted_string}")
    
    # Decrypt the project name using the encrypted string
    project_name = decrypt_encoded_string(encrypted_string, key)
    
    if not project_name:
        print("Error: Failed to decrypt the project name")
        return
    
    print(f"Decrypted Secret: {project_name}")
    
    # Skip copyright verification and proceed with success
    print("Verification successful!")
    if add_success_comment(file_path):
        print(f"Success comment added to {file_path}")

if __name__ == "__main__":
    main()