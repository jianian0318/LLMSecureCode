from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generate an RSA private key
    priv_key = RSA.generate(2048)

    return priv_key.exportKey('OpenSSH')