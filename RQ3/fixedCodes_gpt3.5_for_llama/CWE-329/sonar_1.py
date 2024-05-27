from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def getEncryptionKey(password):
    salt = b'saltysalt'
    iterations = 100000
    backend = default_backend()
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=backend
    )
    
    key = kdf.derive(password)
    
    # Create a Cipher using AES and CBC mode
    iv = b'\x00' * 16
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Encrypt the key using the cipher
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(key) + padder.finalize()
    encrypted_key = encryptor.update(padded_data) + encryptor.finalize()
    
    return encrypted_key