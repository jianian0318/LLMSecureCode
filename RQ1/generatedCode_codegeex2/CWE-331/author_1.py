import random
import string


def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    '''
    letters = string.ascii_letters # Define the set of characters that can be used in the string.
    result = ''.join(random.choice(letters) for i in range(length)) # Generate a string of random characters.

    return result