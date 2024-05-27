def generate_private_key():
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    # Generate a private key using DSA
    private_key = DSA.generate(2048)

    # Export the key using the OpenSSH format
    private_key_export = private_key.export_key(format='OpenSSH')

    # Return the private key
    return private_key_export