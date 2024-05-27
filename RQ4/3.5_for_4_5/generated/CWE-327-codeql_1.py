import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def send_encrypted(secret_key, channel, message):
    '''
    Encrypts the message using AES architecture after creating a cipher,
    and sends it over the channel passed as parameter.
    '''

    # make sure the secret_key is 16 bytes
    secret_key = secret_key[:16]
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
    cipher_encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    # for AES, the data length must be a multiple of 16
    # if it's not, then it must be padded
    message = message.encode('utf-8')
    padded_message = padder.update(message) + padder.finalize()
    encrypted_message = cipher_encryptor.update(padded_message) + cipher_encryptor.finalize()

    # we will send: encrypted_message + iv
    full_message = base64.b64encode(iv + encrypted_message).decode('utf-8')

    # assuming the channel is a function that accepts a string as parameter
    channel(full_message)