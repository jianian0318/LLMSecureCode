# The major issue lays on the LDAP query construction, where no sort of sanitation or safety measures are applied, hence, it leaves room for LDAP Injection. Let's provide a safe input sanitation:

from flask import request, Flask
import ldap
from ldap import filter

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    dc = filter.escape_filter_chars(request.args.get('dc'))
    username = filter.escape_filter_chars(request.args.get('username'))

    query = f"uid={username},ou=people,dc={dc},dc=com"

    ldap_connection = ldap.initialize("ldap://localhost/")
    ldap_connection.simple_bind_s("", "")

    result = ldap_connection.search_s("dc=com", ldap.SCOPE_SUBTREE, query)

    if result:
        return result
    else:
        return "User not found"

# In the fixed code, we are using the built-in `escape_filter_chars()` function from `ldap.filter` to sanitize the string containing the username and domain component from the request. This helps prevent LDAP Injection by escaping the data that is fed into the LDAP system.