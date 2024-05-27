def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Compute the hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Compare the computed hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False