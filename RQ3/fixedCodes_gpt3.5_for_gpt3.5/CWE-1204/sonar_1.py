from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def getEncryptionKey(data, key):
    '''
    Create a random initialization vector (IV), cipher using AES and CBC mode
    encrypt the data using the cipher by padding up to the block_size, and return it
    '''
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data