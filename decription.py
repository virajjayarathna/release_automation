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
    
