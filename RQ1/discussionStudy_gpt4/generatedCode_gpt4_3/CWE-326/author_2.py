from Crypto.PublicKey import DSA
from Crypto.IO import PEM

def generate_private_key():
    key = DSA.generate(2048)
    private_key = key.export_key(format='PEM')
    return private_key

print(generate_private_key())