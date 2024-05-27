from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Getting the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Creating an LDAP query with dc and username
    query = f"(uid={username},{dc})"

    # Establishing an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    # Searching for the user in the LDAP
    result = con.search_s(dc, ldap.SCOPE_SUBTREE, query)

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)
'''
Please replace `ldap://localhost` with your LDAP server address and specify the bind (authentication) process if needed. Also, be aware of the structure of your LDAP directory to adjust the search query if necessary.
'''