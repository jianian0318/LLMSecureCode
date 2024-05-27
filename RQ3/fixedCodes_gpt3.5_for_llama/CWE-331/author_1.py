import random
import string


def generateRandomString(length):
    return ''.join(random.SystemRandom().choices(string.ascii_letters, k=length))


print(generateRandomString(10))