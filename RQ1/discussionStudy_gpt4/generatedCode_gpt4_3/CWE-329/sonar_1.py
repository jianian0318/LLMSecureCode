import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    # Create a random initialization vector
    iv = os.urandom(16)

    # Create a Cipher using AES and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a padder instance
    padder = padding.PKCS7(128).padder()

    # Add padding to the key
    key = padder.update(key) + padder.finalize()

    # Encrypt the key using this cipher
    encryptor = cipher.encryptor()
    encrypted_key = encryptor.update(key) + encryptor.finalize()

    return encrypted_key, iv