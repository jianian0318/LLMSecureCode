from Crypto.PublicKey import DSA
from Crypto.PublicKey.DSA import DSAImplementation

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = DSA.generate(2048)
    private_key = key.export_key(format='OpenSSH')
    return private_key
