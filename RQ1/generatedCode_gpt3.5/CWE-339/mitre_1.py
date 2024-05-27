import os
import random


def generateCryptoKey():
    '''
    Generate a random 128-bit key by using the seeds from os.urandom().
    '''
    return os.urandom(16)