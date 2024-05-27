from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Load or generate RSA key pair
private_key = RSA.generate()
public_key = private_key.public_key()

# Encryption and decryption
ciphertext = public_key.encrypt(
   b'hello world',
   padding.OAEP(
      mgf=padding.MGF1(algorithm=hashes.SHA256()),
      algorithm=hashes.SHA256(),
      label=None
   )
)
plaintext = private_key.decrypt(ciphertext)
print(plaintext)

# Signing and verifying signature
signature = private_key.sign(
   b'hello world',
   padding.PSS(
      mgf=padding.MGF1(hashes.SHA256()),
      salt_length=padding.PSS.MAX_LENGTH
   ),
   hashes.SHA256()
)
public_key.verify(
   signature,
   b'hello world',
   padding.PSS(
      mgf=padding.MGF1(hashes.SHA256()),
      salt_length=padding.PSS.MAX_LENGTH
   ),
   hashes.SHA256()
)