from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    if not dc or not username:
        return {'error': 'dc and username must be provided'}, 400

    user_filter = "(&(cn=" + ldap.filter.escape_filter_chars(username) + ")(dc=" + ldap.filter.escape_filter_chars(dc) + "))"

    con = ldap.initialize('ldap://localhost')

    try:
        result = con.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, user_filter)
        return {'user': result}
    except ldap.LDAPError as e:
        return {'error': str(e)}, 500

if __name__ == "__main__":
    app.run()