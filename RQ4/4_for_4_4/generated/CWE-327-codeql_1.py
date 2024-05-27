from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from os import urandom

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Creating the initialisation vector
    iv = urandom(16)

    # Creating AES Cipher using the secret key
    cipher = Cipher(algorithms.AES(secret_key), modes.CFB(iv), backend=default_backend())

    # Encrypting the message
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message) + padder.finalize()
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

    # Sending the encrypted message over the channel
    channel.send(iv + encrypted_message)