from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # create an LDAP query with them
    query = "(cn=" + username + ")"

    # establish an LDAP connection on localhost
    server = ldap3.Server("localhost")
    connection = ldap3.Connection(server, user="cn=admin,dc=" + dc, password="admin")

    # then search for the user in the LDAP and return it
    connection.bind()
    connection.search('dc=' + dc, query, ldap3.SEARCH_SCOPE_WHOLE_SUBTREE)

    return str(connection.entries)

if __name__ == "__main__":
    app.run(debug=True)