from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = RSA.generate(2048)  # Generate a 2048-bit RSA private key
    private_key = key.export_key(format='PEM')  # Export the private key in PEM format
    return private_key