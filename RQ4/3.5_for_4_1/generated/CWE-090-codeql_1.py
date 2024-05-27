from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Getting the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Creating a sanitized version of the username
    sanitized_username = "".join(x for x in username if x.isalnum())

    # Creating an LDAP query with sanitized username
    # Using ldap.filter.escape_filter_chars to escape special characters in the username
    ldap_query = f"(&(objectClass=user)(sAMAccountName={ldap.filter.escape_filter_chars(sanitized_username)}))"

    # Establishing an LDAP connection on localhost
    conn = ldap.initialize('ldap://localhost')

    # Searching for the user in the LDAP
    result = conn.search_s(f'dc={ldap.filter.escape_filter_chars(dc)},dc=com', ldap.SCOPE_SUBTREE, ldap_query)

    # Close the connection to clean up
    conn.unbind_s()

    # Returning the search result
    return str(result)