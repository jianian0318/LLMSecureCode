from Crypto.PublicKey import RSA

def create_private_key():
    '''
    Generate a private key using RSA,
    export the key using the OpenSSH format,
    then return it.
    '''
    key = RSA.generate(2048) # 生成一个2048位的RSA密钥对。
    private_key = key.export_key().decode('utf-8') # 将密钥导出为OpenSSH格式。
    return private_key