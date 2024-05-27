import os
import random


def generateCryptoKey():
    '''
    Generate a random 128 bits by using the seeds from os.urandom().
    '''
    # Generate 16 bytes of random data
    random_bytes = os.urandom(16)

    # Convert the random bytes into a hexadecimal string
    random_hex = random_bytes.hex()

    # Convert the hexadecimal string into an integer
    random_int = int(random_hex, 16)

    # Return the random integer
    return random_int


# Generate a random 128-bit key
key = generateCryptoKey()

# Print the key
print(key)
