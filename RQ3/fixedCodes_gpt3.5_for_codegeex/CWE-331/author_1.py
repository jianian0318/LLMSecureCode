import random
import string

def generateRandomString(length):
    '''
    Return a secure random string that has only ASCII letters with a fixed size equals to length.
    '''
    letters = string.ascii_letters # Define the set of characters that can be used in the string.

    result = ''.join(random.SystemRandom().choice(letters) for _ in range(length)) # Generate a string of random characters using a secure random number generator.

    return result