from flask import request, Flask
from ldap3 import Server, Connection, ALL_ATTRIBUTES, escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Extract the domain component (dc) and username from the request and escape them
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Create an LDAP query using the escaped info
    query = f"(cn={username})"

    # Establish an LDAP connection on localhost
    server = Server('localhost')
    conn = Connection(server, user=f'{dc}\\{username}', auto_bind=True)

    # Search for the user in the LDAP and return the result
    conn.search(dc, query, attributes=ALL_ATTRIBUTES)
    return conn.response

if __name__ == "__main__":
    app.run()