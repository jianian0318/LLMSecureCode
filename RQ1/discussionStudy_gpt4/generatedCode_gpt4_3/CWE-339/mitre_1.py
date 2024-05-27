import os
import random

def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    seed = os.urandom(16)  # Generate a random 128-bit seed
    random.seed(seed)  # Seed the random number generator
    key = random.getrandbits(128)  # Generate a 128-bit random number
    return key