import hashlib, binascii

def get_password_hash(password, salt):
    dk = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return binascii.hexlify(dk)

password = input("Enter your password: ")
salt = 'salt' # This should be unique for each user
hashed_password = get_password_hash(password, salt)
print(hashed_password)