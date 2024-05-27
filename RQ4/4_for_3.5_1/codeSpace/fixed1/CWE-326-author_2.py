from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the PEM format,
    then return it.
    '''
    key = dsa.generate_private_key(key_size=2048, backend=default_backend())
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key