from Crypto.PublicKey import DSA
from Crypto.PublicKey.DSA import DsaKey
from Crypto.IO import PEM

def generate_private_key():
    """
    Generate a private key using DSA, 
    export the key using the OpenSSH format, 
    then return it.
    """
    # Generate a private DSA key
    private_key = DSA.generate(2048)

    # Export the key in PEM format
    private_key_pem = private_key.export_key(format="PEM")

    return private_key_pem