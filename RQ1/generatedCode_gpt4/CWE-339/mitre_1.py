import os
import random


def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    return os.urandom(16)  # 16 bytes is equal to 128 bits.