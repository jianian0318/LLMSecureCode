    from Crypto.PublicKey import RSA

    def create_private_key():
        private_key = RSA.generate(2048)
        return private_key
    