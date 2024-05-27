from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    '''
    Generate a private key using DSA with pyca/cryptography,
    export the key in OpenSSH format, then return it.
    '''
    # Generate a DSA private key with a secure key size
    key = dsa.generate_private_key(key_size=2048)

    # Export the private key in OpenSSH format
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key.decode('utf-8')

# Usage example
private_key = generate_private_key()
print(private_key)