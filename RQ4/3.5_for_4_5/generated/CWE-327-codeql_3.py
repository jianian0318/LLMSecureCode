import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Create a new SHA256 hash object
    sha256_hash = hashlib.sha256()
  
    # Update the hash object with the bytes of the certificate
    sha256_hash.update(certificate.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    certificate_hash = sha256_hash.hexdigest()
  
    # Return True if the known_hash matches the certificate_hash, otherwise return False
    return certificate_hash == known_hash