from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generate a private key using DSA
    private_key = dsa.generate_private_key(key_size=2048)
    private_key_ssh_format = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key_ssh_format