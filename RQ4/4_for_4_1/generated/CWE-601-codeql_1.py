import os
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_next_url():
    # Extract 'next_url' from the request's query parameters, defaulting to '/' if not found
    next_url = request.args.get('next_url', '/')
    # Redirect the user to the specified 'next_url'
    return redirect(next_url)

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1']
    app.run(debug=debug_mode)