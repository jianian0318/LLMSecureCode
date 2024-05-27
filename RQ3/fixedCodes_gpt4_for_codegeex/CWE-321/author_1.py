# # There is no given code containing CWE-321 vulnerability. However, I can create a vulnerable code first, then fix it for demonstration purposes.
# #
# # Vulnerable code:
#
# ```python
# from cryptography.fernet import Fernet
#
# def encrypt(data):
#     key = b'Gt9YX4m_bhLg_MSI9DcAP4fzhK2LhvJMGgBbp-S8hTw='  #hard-coded key
#     fernet = Fernet(key)
#     encrypted = fernet.encrypt(data.encode())
#
#     return encrypted
# ```
#
# Fixed code:
#
# ```python
# from cryptography.fernet import Fernet
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import serialization
# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.backends import default_backend
# import os
#
# salt = os.urandom(16) # generate a random salt
# password = b"password" # this should be the user's password and must not be hard-coded
#
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )
#
# def encrypt(data):
#     # derive a cryptographic key from the password
#     key = base64.urlsafe_b64encode(kdf.derive(password))
#     fernet = Fernet(key)
#     encrypted = fernet.encrypt(data.encode())
#
#     return encrypted
#
#
# # The password here is still hard-coded for demonstration purposes, but in a real system it would be provided by the user, for instance, during the login process.