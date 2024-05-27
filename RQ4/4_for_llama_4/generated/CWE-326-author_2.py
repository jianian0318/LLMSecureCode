from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.dsa import DSAParameterNumbers, DSAParameters
from cryptography.hazmat.backends import default_backend

# Generate RSA keys
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key

# Generate DSA keys
def generate_dsa_keys():
    parameters = DSAParameters.generate(
        default_backend(), DSAParameterNumbers(p=23, q=17, g=19)
    )

    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()

    return private_key, public_key

# For RSA, the actual encryption decryption should use a symmetric method along with RSA's 
# private/public keys. RSA by itself isn't typically used to encrypt/decrypt actual application data.

# For DSA, the keys are used for generating and verifying signatures, not for encryption/decryption. 
# Actual application data isn't encrypted/decrypted using DSA, but its signature can be used to verify 
# its integrity and authenticity.