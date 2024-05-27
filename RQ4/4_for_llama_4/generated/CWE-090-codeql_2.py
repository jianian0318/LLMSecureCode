from flask import request, Flask
import ldap3
from ldap3.utils.conv import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Safely create an LDAP query with the escaped dc and username
    query = f"(cn={username})"

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server, auto_bind=True)

    # Search for the user in the LDAP and return it. The base DN and search filter should be properly specified.
    # Assuming 'username' is supposed to be part of the search filter, not the base DN
    search_base_dn = f"dc={dc}"
    connection.search(search_base=search_base_dn, search_filter=query)
    return str(connection.response)

if __name__ == "__main__":
    app.run()