def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''

    # Create a cipher object using AES encryption algorithm and the secret key
    cipher = AES.new(secret_key)

    # Encrypt the message using the cipher object
    encrypted_message = cipher.encrypt(message)

    # Send the encrypted message over the channel
    channel.send(encrypted_message)