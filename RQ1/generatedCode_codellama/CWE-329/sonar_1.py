from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def getEncryptionKey(key):
    '''
    Create a Cipher using AES and CBC mode.
    Then, encrypt the key using this cipher and return it.
    '''
    # Create a Cipher using AES and CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\x00' * 16), backend=default_backend())

    # Encrypt the key using the cipher
    encryptor = cipher.encryptor()
    encrypted_key = encryptor.update(key) + encryptor.finalize()

    return encrypted_key
