def getContext():
    '''
    Create an OpenSSL context and return it.
    '''
    # 创建一个SSL上下文
    context = SSL.Context(SSL.SSLv23_METHOD)

    # 加载信任库
    context.load_verify_locations("server.crt")

    # 加载私钥和证书
    context.load_cert_chain("server.crt", "server.key")

    return context
