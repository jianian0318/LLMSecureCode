def create_private_key():
    # Generate a private key using RSA
    private_key = RSA.generate(2048)

    # Export the key using the OpenSSH format
    # and return it
    return private_key.export_key('OpenSSH')