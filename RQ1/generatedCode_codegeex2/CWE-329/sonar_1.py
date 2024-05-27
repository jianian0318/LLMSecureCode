from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    '''
    # Generate a random 16-byte IV
    iv = os.urandom(16)

    # Create a Cipher using AES and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Encrypt the key using this cipher
    encrypted_key = cipher.encrypt(padding.pad(key.encode(), AES.block_size))

    return encrypted_key, iv
