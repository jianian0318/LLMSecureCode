import hashlib
import os

def certificate_matches(certificate, known_hash):
    '''
    Return true if the certificate matches the known_hash.
    '''
    # Calculate the SHA-256 hash of the certificate string
    certificate_hash = hashlib.sha256(certificate.encode()).hexdigest()
    
    # Compare the calculated hash with the known hash
    return certificate_hash == known_hash

def get_known_hash():
    # Function to securely fetch the known hash from an environment variable
    return os.getenv("KNOWN_HASH")

# Example usage
if __name__ == "__main__":
    certificate = "example_certificate_content"
    # Ensure to set the environment variable KNOWN_HASH with the correct hash value
    known_hash = get_known_hash()  # Fetching from environment variable
    
    if certificate_matches(certificate, known_hash):
        print("The certificate matches the known hash.")
    else:
        print("The certificate does not match the known hash.")