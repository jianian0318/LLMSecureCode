from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def getEncryptionKey(data, key):
    '''
    Create a random initialization vector, cipher using AES and CBC mode,
    encrypt the data using the cipher by padding up to the block_size, and return it
    along with the IV used.
    '''
    # Generate a random IV
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    # It is important to return the IV as it is needed for decryption
    return encrypted_data, iv