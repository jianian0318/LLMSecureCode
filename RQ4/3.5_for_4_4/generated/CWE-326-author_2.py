from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    
    # Generate a new DSA key
    private_key = dsa.generate_private_key(
        key_size=2048
    )
    
    # Export the private key in OpenSSH format
    private_key_openssh = private_key.private_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    return private_key_openssh