from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend
import os

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''

    # Generate a DSA key
    private_key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    
    # Export the key in the OpenSSH format
    ssh_key = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    return ssh_key

# Test the function
print(generate_private_key())