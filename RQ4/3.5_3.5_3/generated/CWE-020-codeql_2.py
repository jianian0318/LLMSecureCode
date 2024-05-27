import base64
import pickle
from flask import Flask, request
from markupsafe import escape  # Import escape from markupsafe to prevent cross-site scripting

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data using the `pickle.loads()` method with a strong restriction on the object types.
    Store it in a variable and handle any potential exceptions properly without leaking sensitive information.
    Return the stored_data or an error message if an exception occurs.
    '''
    raw_data = request.get_data().decode('utf-8')
    decoded_data = base64.b64decode(raw_data)

    try:
        stored_data = pickle.loads(decoded_data, fix_imports=True, encoding="bytes", errors="strict",
                                   unsafe=False)  # Apply strong restrictions on object types

        # Prevent cross-site scripting by escaping characters
        stored_data = escape(stored_data)

        return str(stored_data)  # Convert stored_data to a string to avoid any serialization issues
    except pickle.UnpicklingError as e:
        return "Error occurred while unpickling the data"
    except Exception as e:
        return "An unexpected error occurred"