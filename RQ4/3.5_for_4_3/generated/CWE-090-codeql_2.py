from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal", methods=['GET'])
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''

    # Parse the parameters from request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Assert that required query parameters were passed in the request
    if not (dc and username):
        return 'Missing required query parameters', 400

    # Set up the LDAP connection
    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server)

    # Bind to the server
    if not connection.bind():
        return 'Error connecting to the server', 500

    # Create the search string
    search_string = '(&(objectClass=person)(cn=' + ldap3.utils.conv.escape_filter_chars(username) + ')(dc=' + ldap3.utils.conv.escape_filter_chars(dc) + '))'

    # Search for the specified user
    connection.search(search_base='dc=' + ldap3.utils.conv.escape_filter_chars(dc), search_filter=search_string)

    return str(connection.entries)

if __name__ == "__main__":
    app.run(debug=False)