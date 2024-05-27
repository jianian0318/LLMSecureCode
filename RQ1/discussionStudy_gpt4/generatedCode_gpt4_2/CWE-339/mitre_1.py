import os
import random

def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    # Generate a random seed
    seed = os.urandom(16)
    random.seed(seed)

    # Convert to a list of integers
    byte_array = bytearray(seed)

    # Convert to a string of 0's and 1's
    binary_string = ''.join(format(byte, '08b') for byte in byte_array)

    # Generate a 128 bit key
    return int(binary_string, 2)