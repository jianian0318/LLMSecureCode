from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_private_key():
    # Generate a DSA private key
    private_key = dsa.generate_private_key(key_size=2048)

    # Serialize the private key in PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Return the private key
    return private_key_pem