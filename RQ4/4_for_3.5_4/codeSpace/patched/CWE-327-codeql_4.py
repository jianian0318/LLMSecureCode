    hash_object = hashlib.sha256(password.encode() + salt.encode())
    password_hash = hash_object.hexdigest()
    return password_hash