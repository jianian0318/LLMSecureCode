import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def getEncryptionKey(key):
    # Create a random initialization vector (IV)
    iv = os.urandom(16)

    # Create a Cipher using AES and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create an encryptor object
    encryptor = cipher.encryptor()

    # Pad the key to fit the AES block size
    padder = padding.PKCS7(128).padder() 
    padded_key = padder.update(key) + padder.finalize()

    # Encrypt the key
    encrypted_key = encryptor.update(padded_key) + encryptor.finalize()
    
    return encrypted_key, iv  # return encrypted key and the iv used.