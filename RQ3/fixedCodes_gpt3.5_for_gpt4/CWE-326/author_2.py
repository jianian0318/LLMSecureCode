from Crypto.PublicKey import DSA
from Crypto.PublicKey.DSA import generate
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from typing import Union
import base64

def generate_private_key() -> Union[str, None]:
    try:
        # Generate private key
        random_generator = Random.new().read
        private_key = DSA.generate(2048, random_generator)

        # Export private key in PEM format
        private_key_pem = private_key.export_key()
    
        return private_key_pem.decode("utf-8")

    except Exception as e:
        print(f"An error occurred while generating DSA private key: {str(e)}")
        return None