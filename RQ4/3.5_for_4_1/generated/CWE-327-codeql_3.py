import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # compute SHA256 hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # compare the computed hash with the known_hash
    if certificate_hash == known_hash:
        return True
    else:
        return False