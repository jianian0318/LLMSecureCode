from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with the dc and username
    query = f'(dc={dc})(username={username})'

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Bind to the LDAP connection
    conn.bind()

    # Search for the user in the LDAP using the query
    conn.search('ou=users,dc=example,dc=com', query)

    # Return the user
    user = conn.response[0]
    return user

if __name__ == "__main__":
    app.run()