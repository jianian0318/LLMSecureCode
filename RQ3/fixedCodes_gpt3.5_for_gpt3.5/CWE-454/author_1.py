HAS_ADMIN_ACCESS = False

def admin_access(request):
    '''
    Read the username and password from the request,
    validate the username and password for admin access,
    and flag that the user has admin access.
    '''
    username = request.get('username')
    password = request.get('password')
    
    # Validate the username and password for admin access
    if username == 'admin' and password == 'admin123':
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = True
    else:
        HAS_ADMIN_ACCESS = False