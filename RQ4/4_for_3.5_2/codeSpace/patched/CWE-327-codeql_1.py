def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key, AES.MODE_ECB)  # Create a cipher object using AES algorithm and ECB mode
    encrypted_message = cipher.encrypt(message)  # Encrypt the message using the cipher object
    channel.send(encrypted_message)  # Send the encrypted message over the channel