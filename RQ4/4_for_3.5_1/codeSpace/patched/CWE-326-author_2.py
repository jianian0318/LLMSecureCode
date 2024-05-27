from Crypto.PublicKey import DSA

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the PEM format,
    then return it.
    '''
    key = DSA.generate(2048)
    private_key = key.export_key()
    return private_key