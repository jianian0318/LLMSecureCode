import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Create the function

    # First, we need to encode the input to byte format, as hashlib.sha256 requires this format
    certificate_byte = certificate.encode()

    # Creat a sha256 hash object
    certificate_hash = hashlib.sha256(certificate_byte)
   
    # Digest the hash object and convert it to hexadecimal for comparison
    certificate_hash_hex = certificate_hash.hexdigest()
    
    # Compare the hashed certificate and the known hash 
    if certificate_hash_hex == known_hash:
        return True
    else:
        return False