from Crypto.PublicKey import RSA

def create_private_key():
    # Generate a private key using RSA
    private_key = RSA.generate(2048)
    
    # Export the key using the OpenSSH format
    ssh_private_key = private_key.export_key(format='PEM')
    
    # Return the key
    return ssh_private_key