from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def getEncryptionKey(data, key):
    IV = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, IV)

    encrypt_data = cipher.encrypt(pad(data, AES.block_size))

    return encrypt_data