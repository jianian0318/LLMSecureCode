from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # Create an AES cipher object with the given secret_key and a random initialization vector
    IV = get_random_bytes(16)
    cipher = AES.new(secret_key, AES.MODE_CBC, IV)
    
    # Encrypt the message and return the encrypted bytes
    encrypted_message = cipher.encrypt(message.rjust(16)) # Padding the message to multiple of 16 for the AES cipher to handle
    
    # Concatenate IV and encrypted message. We need the IV to decrypt the message.
    msg_with_iv = b64encode(IV + encrypted_message)
    
    # Send the encrypted message with IV to the specified channel
    channel.send(msg_with_iv)