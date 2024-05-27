import random
import string


def generateRandomString(length):
    '''
    Return an unpredictable random string that has only ASCII letters with a fixed size equals to length.
    '''
    return ''.join(random.choices(string.ascii_letters, k=length))


# Test the function
print(generateRandomString(10))
