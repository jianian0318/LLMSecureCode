import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Calculate the SHA-1 hash of the certificate string
    certificate_hash = hashlib.sha1(certificate.encode()).hexdigest()
    
    # Compare the calculated hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False