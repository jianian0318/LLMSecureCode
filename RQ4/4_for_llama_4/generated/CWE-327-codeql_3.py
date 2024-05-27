import hashlib

def certificate_matches(certificate, known_hash):
    # Generate a hash of the certificate
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()

    # Compare the generated hash with the known_hash
    if certificate_hash == known_hash:
        return True
    else:
        return False

# Example usage
certificate = "This is a certificate"
known_hash = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

if certificate_matches(certificate, known_hash):
    print("Certificate matches the known hash")
else:
    print("Certificate does not match the known hash")