# The fixed code should sanitize inputs before passing it to the query. Here we can use `escape_filter_chars` method from ldap3 library to avoid LDAP injection.
from flask import request, Flask
import ldap3
from ldap3.utils.conv import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))
    query = f"(cn={username})"
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server, auto_bind=True)
    conn.search(dc, query)
    return conn.response


# In this fixed code, `escape_filter_chars` method makes sure that special characters are properly escaped before passing the input to the query, eliminating possible LDAP injection vulnerabilities.