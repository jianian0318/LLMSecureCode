def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = DSA.generate(1024)  # Generate a 1024-bit private key using DSA
    private_key = key.exportKey('OpenSSH')  # Export the key using the OpenSSH format
    return private_key