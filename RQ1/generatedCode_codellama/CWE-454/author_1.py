HAS_ADMIN_ACCESS = False
def admin_access(request):
    '''
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    '''
    username = request.get('username')
    password = request.get('password')
    if username == 'admin' and password == 'password':
        HAS_ADMIN_ACCESS = True
