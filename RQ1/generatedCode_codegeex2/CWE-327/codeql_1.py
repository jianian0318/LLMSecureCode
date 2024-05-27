from Crypto.Cipher import *


def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    # 创建一个AES加密器对象，使用给定的密钥
    cipher = AES.new(secret_key, AES.MODE_ECB)
    # 加密消息，并返回加密后的字节串
    encrypted_message = cipher.encrypt(message.rjust(16)) # 填充至16的倍数，以便AES加密器处理
    # 发送加密后的消息到指定的channel

    channel.send(encrypted_message)
    