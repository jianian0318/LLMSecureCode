import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''

    # AES requires that plaintexts be a multiple of 16, so we pad with spaces if necessary.
    while len(message) % 16 != 0:
        message += ' '
    
    # Generate a random initialization vector (IV)
    iv = b'0000000000000000'
    
    # Create the AES cipher with CBC mode and initialize it with the secret key and IV
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Encrypt the message
    encrypted_text = encryptor.update(message.encode()) + encryptor.finalize()
    
    # We convert the encrypted message to base64 to make it safely transmittable.
    encrypted_text = base64.b64encode(encrypted_text).decode()
    
    # Emulate the sending of the encrypted message over the channel.
    channel.send(encrypted_text)

# Note: In this case, 'channel' is assumed to be some sort of network socket or similar object with a 'send' method
# The 'secret_key' as well as the 'message' are strings. For AES, the 'secret_key' should be 16, 24 or 32 bytes long.