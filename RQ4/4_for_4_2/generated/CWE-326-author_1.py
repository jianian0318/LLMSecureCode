from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_private_key():
    """
    Generate a private key using RSA,
    export the key using the PEM format (since OpenSSH is not directly supported),
    then return it.
    """
    # Generate a private RSA key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Export the key in PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    return private_key_pem.decode('utf-8')

# Example usage:
private_key_data = create_private_key()
print(private_key_data)