from Crypto.PublicKey import RSA

def create_private_key():
    private_key = RSA.generate(2048)
    private_key_openssh = private_key.export_key("OpenSSH")
    return private_key_openssh

print(create_private_key())