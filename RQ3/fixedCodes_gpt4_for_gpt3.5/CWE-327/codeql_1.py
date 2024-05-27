from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    iv = get_random_bytes(16)
    cipher = AES.new(secret_key, AES.MODE_CBC, iv)
    
    # padding message to fit AES block size
    pad_message = pad(message.encode(), AES.block_size)
    encrypted_message = iv + cipher.encrypt(pad_message) # prepend IV to the encrypted message

    channel.send(encrypted_message)