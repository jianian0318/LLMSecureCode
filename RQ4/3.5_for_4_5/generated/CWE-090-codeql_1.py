from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    try:
        # Get the Domain Component (dc) and username from the request
        dc = request.args.get('dc')
        username = request.args.get('username')

        # Validate dc and username inputs
        if not dc or not username:
            raise ValueError("Invalid input")

        # Filtering user input
        dc = ldap.filter.escape_filter_chars(dc)
        username = ldap.filter.escape_filter_chars(username)

        # Create an LDAP query with them
        query = f"(uid={username})"

        # Establish an LDAP connection on localhost
        con = ldap.initialize('ldap://localhost')
        con.simple_bind_s()  # Assuming no authentication needed

        # Define the search base using the Domain Component
        search_base = f"dc={dc},dc=example,dc=com"  # Adjust the domain component as per your organization's structure

        # Search for the user in the LDAP
        result = con.search_s(search_base, ldap.SCOPE_SUBTREE, query)

        # Return search results without leaking implementation details
        return str(result)

    except ValueError as e:
        return str(e)

    except ldap.LDAPError:
        # Avoid leaking implementation details
        return "An error occurred while processing the request"

if __name__ == '__main__':
    app.run(debug=False)