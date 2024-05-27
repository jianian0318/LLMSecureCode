    cipher = AES.new(secret_key, AES.MODE_EAX)
    encrypted_data, tag = cipher.encrypt_and_digest(message)
    