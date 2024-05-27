def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key)  # Create a cipher object
    encrypted_message = cipher.encrypt(message.encode())  # Encrypt the message
    channel.send(encrypted_message)  # Send the encrypted message over the channel