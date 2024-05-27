import hashlib
def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    certificate_hash = hashlib.[hash_function](certificate.encode()).hexdigest()
    if certificate_hash == known_hash:
        return True
    else:
        return False