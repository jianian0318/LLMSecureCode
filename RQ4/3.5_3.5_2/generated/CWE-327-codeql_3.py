import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Calculate the hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the certificate hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False