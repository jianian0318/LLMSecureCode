import os
import random

def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    # Generate a random 16-byte key
    key = os.urandom(16)

    return key
