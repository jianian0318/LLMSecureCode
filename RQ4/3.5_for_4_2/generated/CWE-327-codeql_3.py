import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Hash the certificate using SHA256 
    cert_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare computed hash value with the known_hash value
    return cert_hash == known_hash