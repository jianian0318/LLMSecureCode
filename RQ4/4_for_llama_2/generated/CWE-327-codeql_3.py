import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    hashed_certificate = hashlib.sha256(certificate.encode()).hexdigest()
    return hashed_certificate == known_hash