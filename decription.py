import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad



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
    

if __name__ == "__main__":
    main()