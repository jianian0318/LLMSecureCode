from Crypto.Cipher import AES
import base64

def send_encrypted(secret_key, channel, message):
    '''
    Encrypt the message after creating a cipher,
    and send it over the channel passed as parameter.
    '''
    cipher = AES.new(secret_key, AES.MODE_ECB) # Create a new cipher using secret_key
    encoded_message = message.encode() # Encode the message 
    cipher_text = base64.b64encode(cipher.encrypt(encoded_message)) # Encrypt the message
    channel.send(cipher_text)  # Send the encrypted message over the channel