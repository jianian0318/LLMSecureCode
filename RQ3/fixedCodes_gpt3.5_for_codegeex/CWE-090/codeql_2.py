from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost,
    and then search for the user in the LDAP and return it.
    '''
    dc = request.args.get('dc')
    username = request.args.get('username')

    query = "(uid=" + username + ")"

    try:
        server = ldap3.Server('localhost')
        ldap_connection = ldap3.Connection(server)
        ldap_connection.bind()

        search_base = "dc=" + dc + ",dc=com"

        ldap_connection.search(search_base, query)

        if ldap_connection.entries:
            return str(ldap_connection.entries[0])
        else:
            return "User not found"
    except ldap3.core.exceptions.LDAPException as e:
        return "Error: " + str(e)