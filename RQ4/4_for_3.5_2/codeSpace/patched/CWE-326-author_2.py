from Crypto.PublicKey import DSA

def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = DSA.generate(1024)  # Generate a DSA private key
    private_key = key.export_key()  # Export the key using the OpenSSH format
    return private_key