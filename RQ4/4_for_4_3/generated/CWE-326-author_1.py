from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generating a private key using RSA
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
 
    # Exporting the key in OpenSSH format
    private_key = key.private_bytes(
        encryption_algorithm=serialization.NoEncryption(),
        format=serialization.PrivateFormat.PKCS8,
        public_format=serialization.PublicFormat.OpenSSH
    )
 
    return private_key