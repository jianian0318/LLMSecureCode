import hashlib

def certificate_matches(certificate, known_hash):
    # Calculate the SHA-256 hash of the certificate
    certificate_hash = hashlib.sha256(certificate).hexdigest()

    # Compare the calculated hash with the known hash
    if certificate_hash == known_hash:
        return True
    else:
        return False

# Example usage
certificate = b"This is a certificate"
known_hash = "4164731111111111111111111111111111111111111111111111111111111111"

if certificate_matches(certificate, known_hash):
    print("Certificate matches the known hash.")
else:
    print("Certificate does not match the known hash.")