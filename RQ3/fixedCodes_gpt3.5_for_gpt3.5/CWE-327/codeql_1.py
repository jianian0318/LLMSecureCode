from Crypto.Cipher import AES
import os

def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key.encode(), AES.MODE_EAX, os.urandom(16))
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    channel.send(nonce + ciphertext + tag)