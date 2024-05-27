from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/')
def index():
    # Get the User-Agent from the request headers and escape it to prevent XSS attacks
    user_agent = request.headers.get('User-Agent', 'UnknownAgent')
    safe_user_agent = escape(user_agent)
    
    # Instead of using exec() to dynamically import libraries, handle imports statically
    # and just print what the incoming User-Agent is. 
    # Note: If module-specific behavior is required, implement controlled, secure conditions.

    return "User-Agent: {}".format(safe_user_agent)

if __name__ == '__main__':
    app.run()