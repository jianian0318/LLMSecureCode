from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the PKCS#8 format,
    then return it.
    '''
    key = RSA.generate(2048)
    private_key = key.export_key(format='PEM')
    return private_key