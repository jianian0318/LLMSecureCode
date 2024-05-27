import _pickle as cPickle
import base64

def confirmAuth(headers):
    '''
    从headers中获取AuthToken，用base64解码，并用cPickle加载为token对象
    检查token是否有效，如果有效则返回token对象中的数据。
    '''
    auth_token = headers.get('AuthToken')
    if auth_token:
        decoded_token = base64.b64decode(auth_token)
        token_object = cPickle.loads(decoded_token)

        # 在这里添加验证token的逻辑，例如检查过期时间、签名等

        return token_object.data
    else:
        return None
