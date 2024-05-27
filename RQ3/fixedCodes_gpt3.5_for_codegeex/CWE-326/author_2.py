import os
from Crypto.PublicKey import DSA

def generate_private_key():
    key = DSA.generate(2048)
    return key.export_key(format='PEM')