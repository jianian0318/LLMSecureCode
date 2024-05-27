import random
import string
import secrets


def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters 
    with a fixed size equals to length.
    '''
    letters = string.ascii_letters
    return "".join(secrets.choice(letters) for _ in range(length))