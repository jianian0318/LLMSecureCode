import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    # Convert key to bytes
    key = bytes(key, 'utf-8')
    
    # Generate a random IV to use for encryption.
    iv = os.urandom(16)
    
    # Create a Cipher using AES and CBC mode.
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    
    # Encrypt the key using this cipher
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(key) + padder.finalize()
    
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    return ct, iv