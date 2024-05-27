import hashlib


def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Create a hash object
    hash_object = hashlib.sha256()

    # Calculate the hash of the certificate string
    hash_object.update(certificate.encode('utf-8'))
    certificate_hash = hash_object.hexdigest()

    # Compare the certificate hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False