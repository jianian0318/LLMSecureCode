from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    # Generate a new DSA key pair
    private_key = dsa.generate_private_key(key_size=2048)

    # Export the private key in PEM format
    private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.PKCS8,
                                                encryption_algorithm=serialization.NoEncryption())

    # Return the private key
    return private_key_pem