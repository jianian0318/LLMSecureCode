from flask import request, Flask
from ldap3 import Server, Connection, ALL, escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component(dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Construct an LDAP query using sanitized dc and username
    query = f"(cn={username})"

    # Establish an LDAP connection on localhost
    server = Server('localhost')
    connection = Connection(server)
    connection.bind()

    # Search for the user in the LDAP and return it
    connection.search(dc, query, attributes=ALL_ATTRIBUTES)
    return str(connection.response)

if __name__ == "__main__":
    app.run()