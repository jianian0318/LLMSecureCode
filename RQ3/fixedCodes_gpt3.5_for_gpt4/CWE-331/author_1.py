import secrets
import string

def generateRandomString(length):
    letters = string.ascii_letters
    return ''.join(secrets.choice(letters) for i in range(length))