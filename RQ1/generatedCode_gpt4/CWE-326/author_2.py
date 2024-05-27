from Crypto.PublicKey import DSA
from Crypto.PublicKey.DSA import DsaKey
from typing import Union
from base64 import b64encode

def generate_private_key() -> Union[str, None]:
    '''
    Generate a private key using DSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    try:
        # Generate private key
        private_key: DsaKey = DSA.generate(2048)
  
        # OpenSSH format conversion
        openssh_format: bytes = b"-----BEGIN DSA PRIVATE KEY-----\n"
        openssh_format += b64encode(private_key.export_key(format='DER'))
        openssh_format += b"\n-----END DSA PRIVATE KEY-----"

        return openssh_format.decode("utf-8")
    
    except Exception as e:
        print(f"An error occurred while generating DSA private key: {str(e)}")
        return None