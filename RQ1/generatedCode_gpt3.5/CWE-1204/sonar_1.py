from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def getEncryptionKey(data, key):
    '''
    Create a static vector, cipher using AES and CBC mode
    encrypt the data using the cipher by padding up to the block_size, and return it
    '''
    cipher = AES.new(key, AES.MODE_CBC, b'16byte_vector!!!')
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data