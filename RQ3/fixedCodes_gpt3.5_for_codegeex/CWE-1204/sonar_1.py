from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os


def getEncryptionKey(data, key):
    '''
    Create a random initialization vector (IV) using os.urandom() function
    cipher using AES and CBC mode
    encrypt the data using the cipher by padding up to the block_size, and return it
    '''
    iv = os.urandom(16)  # random initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size))