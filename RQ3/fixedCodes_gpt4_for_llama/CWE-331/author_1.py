import os
import string

def generateSecureRandomString(length):
    '''
    Return a secure random string that has only ASCII letters with a fixed size equals to length.
    '''
    return ''.join(os.urandom(length).decode('latin1') for i in range(length))

# Test the function
print(generateSecureRandomString(10))