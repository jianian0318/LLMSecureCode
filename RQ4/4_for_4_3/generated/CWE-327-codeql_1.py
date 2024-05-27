from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Assuming secret_key is a 16, 24, or 32 bytes long for AES
    # Create a new cipher object using the secret key
    cipher = Cipher(algorithms.AES(secret_key), modes.CBC(secret_key), backend=default_backend())

    # Create an encriptor
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()

    # Encrypt the message
    encrypted_message = encryptor.update(padded_data) + encryptor.finalize()
    
    channel(encrypted_message)

# Example usage:
# Assuming 'channel' is a defined function that sends bytes:
# def channel(data):
#     print("Sending encrypted data:", data)

# secret_key must be a bytes object of the appropriate length for AES (e.g., 16, 24, or 32 bytes)
# For this example, a 16-bytes long key will be randomly generated:
# secret_key = os.urandom(16)

# You would typically use the function like this:
# send_encrypted(secret_key, channel, "Your secret message here")