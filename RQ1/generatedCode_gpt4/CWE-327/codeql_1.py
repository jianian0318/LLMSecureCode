from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(bytes(message, 'utf-8'))

    # Usually, this is where you'd store or send your (nonce, ciphertext, tag) values.
    # As we are running this as script, we're simply going to print it out
    print("Sent over channel:", nonce, ciphertext, tag)