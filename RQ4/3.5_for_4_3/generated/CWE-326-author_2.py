from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    '''
    Generate a private key using RSA,
    export the key using the PKCS8 serialization format,
    then return it.
    '''
    # Generate an RSA key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Export the private key in the PKCS8 serialization format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    return private_key_pem