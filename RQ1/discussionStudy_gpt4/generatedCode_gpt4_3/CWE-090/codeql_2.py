from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with them
    search_filter = "(uid={0})".format(username)
    search_base = "dc={0},dc=com".format(dc)

    # Establish an LDAP connection on localhost
    server = ldap3.Server("localhost")
    with ldap3.Connection(server) as conn:
        # Search for the user in the LDAP and return it
        conn.search(search_base, search_filter)
        return str(conn.entries)

if __name__ == "__main__":
    app.run(debug=True)