from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generate a DSA key
    key = dsa.generate_private_key(key_size=2048)

    # Convert to OpenSSH format
    openssh_key = key.private_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )

    return openssh_key