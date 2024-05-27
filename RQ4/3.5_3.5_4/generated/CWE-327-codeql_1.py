def send_encrypted(secret_key, channel, message):
    # Create a cipher object using the provided secret_key
    cipher = AES.new(secret_key, AES.MODE_ECB)

    # Encrypt the message using the cipher
    encrypted_message = cipher.encrypt(message)

    # Send the encrypted message over the channel
    channel.send(encrypted_message)