from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.backends import default_backend

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the PEM format,
    then return it.
    '''
    # Generate a private key
    private_key = dsa.generate_private_key(
        key_size=2048,
        backend=default_backend()
    )

    # Convert the private key to PEM format
    key_string = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    return key_string