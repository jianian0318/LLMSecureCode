from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from os import urandom

backend = default_backend()

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''

    # Convert message to bytes, if not already
    if not isinstance(message, bytes):
        message = message.encode('utf-8')

    # Generate a random 96-bit IV.
    iv = urandom(12)

    # Create an AES-GCM Cipher.
    cipher = Cipher(algorithms.AES(secret_key), modes.GCM(iv), backend=backend)

    # Create a Padder instance
    padder = padding.PKCS7(128).padder()

    # Pad the data
    padded_data = padder.update(message) + padder.finalize()

    # Encrypt the padded message
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

    # Send encrypted message over channel
    channel.send(iv + encrypted_message)