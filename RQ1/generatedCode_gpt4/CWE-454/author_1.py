# Initialization of some constant admin username and password
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_access(request):
    '''
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    '''

    # Getting Username & Password from the request
    username = request.get('username')
    password = request.get('password')
    
    # Initialize flag variable
    global HAS_ADMIN_ACCESS
    
    # validate username and password
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        HAS_ADMIN_ACCESS = True # Admin Access granted as valid credentials.
    else:
        HAS_ADMIN_ACCESS = False # No admin access as invalid credentials
    
    return HAS_ADMIN_ACCESS

# Simulate a request
request = {'username': 'admin', 'password': 'admin123'}
print(admin_access(request))  # The output should be True because the passed request has correct admin credentials.