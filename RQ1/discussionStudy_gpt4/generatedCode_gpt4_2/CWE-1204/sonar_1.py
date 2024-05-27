from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def getEncryptionKey(data, key):
    static_vector = 'abcdefghijklmnop'  # 16 bytes long static vector
    cipher = AES.new(key, AES.MODE_CBC, static_vector)  
    padded_data = pad(data, AES.block_size)  # Padding data up to block_size
    encrypted_data = cipher.encrypt(padded_data)  # Encrypting padded data

    return encrypted_data