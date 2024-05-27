# The fixed code that sanitizes inputs to avoid LDAP Injection is as follows:

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

    query = f"uid={username},ou=people,dc={dc},dc=com"

    ldap_connection = ldap3.initialize("ldap://localhost/")
    ldap_connection.simple_bind_s("", "")

    result = ldap_connection.search_s("dc=com", ldap3.SCOPE_SUBTREE, query)

    if result:
        return result
    else:
        return "User not found"


# In this code, the ldap3.utils.conv.escape_filter_chars() function is used to sanitize the inputs for 'dc' and 'username' that will be part of the LDAP query. The function escape_filter_chars() will escape any special characters that could be in the input strings and avoid potential LDAP Injection attacks.