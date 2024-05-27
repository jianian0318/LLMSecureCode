from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    
    # Generate random bytes for the initialization vector (IV)
    iv = get_random_bytes(16)
    
    # Create a new AES cipher with the secret_key and IV
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
    
    # Create a encryptor object from the cipher
    encryptor = cipher.encryptor()

    # Encrypt the message
    ciphertext = encryptor.update(message) + encryptor.finalize()
    
    # Send the encrypted message over the channel
    channel.send(ciphertext)