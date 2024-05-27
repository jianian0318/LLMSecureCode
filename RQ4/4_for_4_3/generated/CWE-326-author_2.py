from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the PEM format,
    then return it.
    '''
    # Generate a new DSA key
    key = dsa.generate_private_key(key_size=2048)

    # Export the key in PEM format
    private_key = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    return private_key.decode('utf-8')

# Use the function and print the generated private key
if __name__ == '__main__':
    private_key = generate_private_key()
    print(private_key)