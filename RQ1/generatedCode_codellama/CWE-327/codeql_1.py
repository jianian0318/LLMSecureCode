from Crypto.Cipher import AES


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key, AES.MODE_EAX)
    encrypted_data, tag = cipher.encrypt_and_digest(message)
    channel.send(encrypted_data)
    channel.send(tag)
    channel.send(cipher.nonce)
