from Crypto.PublicKey import DSA

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = DSA.generate(2048)  # Generate a DSA private key with 2048-bit size
    private_key = key.export_key()  # Export the private key in PEM format
    return private_key