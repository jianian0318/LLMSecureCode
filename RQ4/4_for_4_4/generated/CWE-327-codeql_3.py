import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Convert the certificate to bytes and hash it using SHA256
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the generated hash with the known_hash
    if certificate_hash == known_hash:
        return True
    else:
        return False