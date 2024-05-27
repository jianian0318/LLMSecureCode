import hashlib

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Calculate the SHA-256 hash of the certificate string
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the calculated hash with the known hash
    return certificate_hash == known_hash

# Example usage
if __name__ == "__main__":
    certificate = "example_certificate_content"
    known_hash = "d5a295e205c585df62e16653b14754f63fcbcf8a38615db77ea0c03e6b46f1d4"  # SHA-256 hash for the example
    
    if certificate_matches(certificate, known_hash):
        print("The certificate matches the known hash.")
    else:
        print("The certificate does not match the known hash.")