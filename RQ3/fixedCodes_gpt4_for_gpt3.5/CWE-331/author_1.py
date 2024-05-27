import os
import string

def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    '''
    letters = string.ascii_letters
    return ''.join(letters[ord(os.urandom(1)) % len(letters)] for _ in range(length))