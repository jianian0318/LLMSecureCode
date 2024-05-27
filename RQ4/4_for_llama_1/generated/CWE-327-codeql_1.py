from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def send_encrypted(secret_key, channel, message):
    # Create a padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()
    
    # Create a cipher using the secret key
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(b"\0" * 16), backend=default_backend())
    
    # Create an encryptor object
    encryptor = cipher.encryptor()
    
    # Encrypt the message using the cipher
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    
    # Send the encrypted message
    channel.send(encrypted_message)