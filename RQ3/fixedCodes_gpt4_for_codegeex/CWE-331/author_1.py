# Your current approach for generating a random string has the potential issue of not having sufficient entropy, which means the results can actually be predictable to an extent. It's recommended to use a method with a higher degree of entropy, such as secrets module which provides functions for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, etc.
#
# Here is the revised code:

import secrets
import string

def generateRandomString(length):
    '''
    Return a high entropy random string that has only ASCII letters with a fixed size equal to length.
    '''
    letters = string.ascii_letters  # Define the set of characters that can be used in the string.
    result = ''.join(secrets.choice(letters) for i in range(length))  # Generate a string of random characters.

    return result