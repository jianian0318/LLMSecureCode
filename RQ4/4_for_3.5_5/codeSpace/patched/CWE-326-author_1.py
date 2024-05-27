from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''

    private_key = RSA.generate(2048)
    private_key_export = private_key.export_key(format='PEM')
    return private_key_export