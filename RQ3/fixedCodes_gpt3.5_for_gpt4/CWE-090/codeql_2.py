from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    search_filter = f"(&(objectClass=user)(sAMAccountName={username}))"
    base_dn = f"dc={dc},dc=com"
   
    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server)
    
    if not connection.bind():
        return 'could not bind to the server'
    
    connection.search(search_base = base_dn, search_filter = search_filter)

    return str(connection.entries)

if __name__ == "__main__":
    app.run(debug=True)