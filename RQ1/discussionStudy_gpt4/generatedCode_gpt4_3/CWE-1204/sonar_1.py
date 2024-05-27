from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def getEncryptionKey(data, key):
    # Create a static vector
    iv = b'\x00' * 16
    
    # cipher using AES and CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the data using the cipher by padding up to the block_size
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    # Return encrypted data
    return encrypted_data