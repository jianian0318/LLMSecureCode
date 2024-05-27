from flask import request, Flask
import ldap3
import re

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Fixed: Validate the dc and username to ensure only alphanumeric characters are allowed
    # to remove the possibility of LDAP injection attacks
    dc = re.sub(r'\W+', '', dc)
    username = re.sub(r'\W+', '', username)

    # Fixed: Construct the LDAP query safely
    ldap_query = f'(uid={ldap3.utils.conv.escape_filter_chars(username)},dc={ldap3.utils.conv.escape_filter_chars(dc)})'

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost', use_ssl=False)
    conn = ldap3.Connection(server, auto_bind=True)  # Fixed: Added auto_bind=True to establish connection
    
    # Search for the user in the LDAP and return it
    conn.search(ldap_query, '(objectclass=*)', attributes=[ldap3.ALL_ATTRIBUTES])  # Fixed: Correct LDAP search base and filter
    if conn.entries:
        # If the user is found, return its details.
        return str(conn.entries[0]), 200
    else:
        # If the user is not found, return an error message.
        return "User not found", 404

if __name__ == '__main__':
    # Fixed: Limit the server to only be accessible from the local machine
    app.run(host='127.0.0.1', port=5000)