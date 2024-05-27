from flask import Flask, request
import ldap
import re

app = Flask(__name__)

def sanitize_dn(value):
    if len(value) > 500: # preventing long strings
       return BadRequest('Value is too long')
    value = re.sub(r'([,\\#+<>;"=])', r'\\\1', value)
    value = re.sub(r'^\s+|\s+$', r'\\\0', value)
    value = re.sub(r'^#', r'\#', value)
    value = value.replace('\x00', '\\00')
    return value

@app.route("/normal")
def normal():
    username = sanitize_dn(request.args.get('username'))
    dc = sanitize_dn(request.args.get('dc'))

    ldap_filter = f"(uid={username},dc={dc})"
    base_dn = ""

    con = ldap.initialize('ldap://localhost')

    try:
        result = con.search_s(base_dn, ldap.SCOPE_SUBTREE, ldap_filter)
    except ldap.LDAPError:
        return "An LDAP error occurred."
    finally:
        con.unbind()

    return str(result)

if __name__ == "__main__":
    app.run(debug=False)