from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # get the Domain Component (dc) and username from the request,
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # create an LDAP query with them,
    search_filter = f"(sAMAccountName={username})"
    base_dn = f"dc={dc},dc=com"
   
    # establish an LDAP connection on localhost, 
    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server)
    
    # connect and bind to the server
    if not connection.bind():
      return 'could not bind to the server'
    
    # then search for the user in the LDAP and return it.
    connection.search(search_base = base_dn, search_filter = search_filter)

    return str(connection.entries)

if __name__ == "__main__":
    app.run(debug=True)