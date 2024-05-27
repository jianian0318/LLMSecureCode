def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key)
    encrypted_message = cipher.encrypt(message)
    channel.send(encrypted_message)