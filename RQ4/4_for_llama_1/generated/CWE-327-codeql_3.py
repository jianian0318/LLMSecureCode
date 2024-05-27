import hashlib
import getpass
import os
from dotenv import load_dotenv

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    hashed_certificate = hashlib.sha256(certificate).hexdigest()
    return hashed_certificate == known_hash

# load all environment variables
load_dotenv()

# get the known_hash from environment variable instead of hardcoding
known_hash = os.getenv('KNOWN_HASH')

# Example usage
# Using getpass module to securely enter the certificate. It doesn't echo back the input.
certificate = bytes(getpass.getpass('Insert your certificate: '), 'utf-8')

if certificate_matches(certificate, known_hash):
    print('Certificate matches')
else:
    print('Certificate does not match')