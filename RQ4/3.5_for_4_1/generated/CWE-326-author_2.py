from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
import os

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''

    # Generate the key
    key = dsa.generate_private_key(key_size=2048)

    # Export the key in OpenSSH format
    private_key_openssh = key.private_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Return the keys
    return private_key_openssh