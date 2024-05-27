# Define username and password for admin
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

HAS_ADMIN_ACCESS = False

def admin_access(request):
    username = request['username']
    password = request['password']

    # Validate username and password
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        # If validated, flag the user has admin access
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = True
        return "Admin access granted"
    else:
        return "Invalid credentials"