import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Calculate the hash of certificate and compare it with the known_hash.
    Return true if the certificate matches the known_hash.
    '''

    # calculate the hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # compare the calculated hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False