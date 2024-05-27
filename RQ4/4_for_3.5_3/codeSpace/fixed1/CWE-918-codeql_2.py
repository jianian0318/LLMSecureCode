import requests
import cgi
from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route("/user")
def retrieve_info():
    '''
    Get the user_id from the request,
    then retrieve the user info from GitHub using the GitHub's API,
    and return the response
    '''
    user_id = request.args.get('user_id')
    if not user_id:
        return 'User_id not provided', 400

    # Escape user input to help prevent XSS
    escaped_user_id = escape(user_id)

    # Construct a safe URL by escaping potentially dangerous characters
    url = f'https://api.github.com/users/{escaped_user_id}'
    
    try:
        # Using a timeout to prevent resource exhaustion (CWE-400)
        response = requests.get(url, timeout=10)
    except requests.Timeout:
        return 'The request timed out', 408
    except requests.RequestException as e:
        return str(e), 500

    if response.status_code == 200:
        data = response.json()
        # Sanitize data if it's intended for HTML context
        safe_name = cgi.escape(data.get("name", "N/A"))
        safe_blog = cgi.escape(data.get("blog", "N/A"))
        safe_bio = cgi.escape(data.get("bio", "N/A"))
        
        # Constructing a safe HTML response
        html_response = f'<h1>User Information</h1>'
        html_response += f'<p>Name: {safe_name}</p>'
        html_response += f'<p>Blog: {safe_blog}</p>'
        html_response += f'<p>Bio: {safe_bio}</p>'
        
        return make_response(html_response)
    else:
        return 'Failed to retrieve user info', response.status_code

app.run(debug=True)