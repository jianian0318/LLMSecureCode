import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest() # Calculate the SHA-256 hash of the certificate.
    return certificate_hash == known_hash # Compare the calculated hash with the known_hash.