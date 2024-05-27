import base64
import pickle
from flask import Flask, request
from itsdangerous import BadSignature, SignatureExpired
from itsdangerous import TimedSafeSerializer as Serializer

app = Flask(__name__)
app.secret_key = 'your secret key'
serializer = Serializer(app.secret_key)

@app.route("/profile")
def profile():
    raw_data = request.get_data().decode('utf-8')
    try:
        session_cookie = serializer.loads(raw_data)
    except SignatureExpired:
        return 'The session cookie has expired' 
    except BadSignature:
        return 'The session cookie is invalid' 
    
    decoded_data = base64.b64decode(session_cookie)
    try:
        deserialized_data = pickle.loads(decoded_data)
    except (pickle.UnpicklingError, AttributeError, EOFError, ImportError, IndexError):
        return 'Deserialization error'
        
    return str(deserialized_data)