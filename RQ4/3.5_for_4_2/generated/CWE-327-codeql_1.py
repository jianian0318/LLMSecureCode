from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def send_encrypted(secret_key, channel, message):
    cipher = Cipher(algorithms.AES(secret_key), modes.EAX(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    tag = encryptor.tag
    
    channel.send({'ciphertext': ciphertext, 'tag': tag})