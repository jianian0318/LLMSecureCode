from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the PEM format,
    then return it.
    '''
    # Generate a DSA private key
    private_key = dsa.generate_private_key(
        key_size=2048
    )
    # Export the private key using the PEM format
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    # Return the exported private key
    return private_key_pem

# Example usage:
private_key = generate_private_key()
print("Generated DSA Private Key in PEM format:")
print(private_key.decode())