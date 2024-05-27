import random
import string

def generateRandomString(length):
    # Using random.choices()
    # Generating random strings
    return ''.join(random.choices(string.ascii_letters, k=length))