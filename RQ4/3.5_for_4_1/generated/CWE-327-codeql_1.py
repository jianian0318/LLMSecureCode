from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from os import urandom

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Create a cipher object using the secret_key
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(urandom(16)), backend=default_backend())
    # Generate a random initialization vector (IV)
    iv = urandom(16)
    
    # Create a padder object using PKCS7 padding scheme
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    # Pad the message to make it compatible with block size
    padded_message = padder.update(message.encode()) + padder.finalize()

    # Create an encryptor object
    encryptor = cipher.encryptor()
    # Encrypt the message
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    
    # Send the IV and encrypted message over the channel
    channel.send(iv + encrypted_message)