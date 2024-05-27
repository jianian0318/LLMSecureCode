    cipher = AES.new(secret_key, AES.MODE_EAX)
    encrypted_message, tag = cipher.encrypt_and_digest(message)
    