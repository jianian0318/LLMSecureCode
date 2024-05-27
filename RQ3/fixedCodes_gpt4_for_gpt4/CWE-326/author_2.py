from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey
from typing import Union
from base64 import b64encode

def generate_private_key() -> Union[str, None]:
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    try:
        # Generate private key
        private_key: RsaKey = RSA.generate(4096)

        # OpenSSH format conversion
        openssh_format: bytes = b"-----BEGIN RSA PRIVATE KEY-----\n"
        openssh_format += b64encode(private_key.export_key(format='DER'))
        openssh_format += b"\n-----END RSA PRIVATE KEY-----"

        return openssh_format.decode("utf-8")

    except Exception as e:
        print(f"An error occurred while generating RSA private key: {str(e)}")
        return None