def send_encrypted(secret_key, channel, message):
    cipher = AES.new(secret_key, AES.MODE_ECB)
    encrypted_message = cipher.encrypt(message)
    channel.send(encrypted_message)