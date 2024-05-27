import base64
import pickle

from flask import Flask, request, escape

app = Flask(__name__)

def sanitize_input(user_input):
    '''
    Sanitizes user input by escaping special characters
    '''
    return escape(user_input)

@app.route("/profile", methods=["POST"])
def profile():
    '''
    Get raw_data from request, sanitize it, deserialize it and return it
    '''
    try:
        # Getting base64 encoded string from request data
        b64_encoded_str = request.get_data(as_text=True)
        
        # Decoding base64 string
        decoded_str = base64.b64decode(b64_encoded_str).decode("utf-8")
        
        # Deserialization / unpickling
        profile_info = pickle.loads(decoded_str)
        
        # Sanitize profile_info
        sanitized_info = sanitize_input(profile_info)
        
        return sanitized_info
    except (base64.binascii.Error, ValueError, pickle.UnpicklingError, UnicodeDecodeError, TypeError):
        return "Invalid data"