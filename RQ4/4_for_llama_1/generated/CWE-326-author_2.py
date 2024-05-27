from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa, rsa
import base64

# Generate a DSA key
private_key_dsa = dsa.generate_private_key(
    key_size=2048,
    backend=default_backend()
)

# Generate a RSA key
private_key_rsa = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

# Serialize the keys
private_key_dsa_pem = private_key_dsa.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

private_key_rsa_pem = private_key_rsa.private_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PrivateFormat.PKCS8,
   encryption_algorithm=serialization.NoEncryption()
)

# Base64 encode the keys
encoded_key_dsa = base64.b64encode(private_key_dsa_pem)
encoded_key_rsa = base64.b64encode(private_key_rsa_pem)

print('DSA key:', encoded_key_dsa)
print('RSA key:', encoded_key_rsa)