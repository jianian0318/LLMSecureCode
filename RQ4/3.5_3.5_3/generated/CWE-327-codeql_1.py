from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.backends import default_backend

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Create an AES cipher object with the provided secret key and CBC mode
    backend = default_backend()
    cipher = Cipher(algorithms.AES(secret_key), CBC(), backend=backend)

    # Create an encryptor object from the cipher and initialize it with an IV
    encryptor = cipher.encryptor()
    iv = b'\x00' * 16
    encryptor.authenticate_additional_data(iv) # Authentication of IV for CBC mode

    # Encrypt the message using the encryptor
    encrypted_message = encryptor.update(message) + encryptor.finalize()

    # Send the encrypted message over the channel
    channel.send(encrypted_message)