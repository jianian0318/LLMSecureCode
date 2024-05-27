from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#Generate an RSA keypair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

#Get the public key for exchange
public_key = private_key.public_key()

#Serialize private key for storage
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
)

#Serialize public key for storage
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)