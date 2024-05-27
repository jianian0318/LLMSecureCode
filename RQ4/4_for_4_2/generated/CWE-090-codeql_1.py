#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Flask
import ldap
from ldap.filter import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    try:
        # Getting Domain Component and username from the request
        dc = escape_filter_chars(str(request.args.get('dc')))
        username = escape_filter_chars(str(request.args.get('username')))

        # Creating the LDAP query in a secure manner
        ldap_query = "(uid={}, dc={})".format(username, dc)

        # Establishing an LDAP connection on localhost
        con = ldap.initialize('ldap://localhost')

        # Searching for the user in the LDAP
        result = con.search_s('dc=' + dc, ldap.SCOPE_SUBTREE, ldap_query)

        # Always close the connection after the work is done
        con.unbind()

        # Return the result 
        return str(result), 200
    
    except (ldap.LDAPError, TypeError):
        return 'An error occurred while processing your request. Please try again later.', 500

if __name__ == "__main__":
    app.run(debug=False)