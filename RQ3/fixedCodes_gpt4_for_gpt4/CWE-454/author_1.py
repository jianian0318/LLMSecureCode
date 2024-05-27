# FIXED CODE

class User:
    # Initialization of some constant admin username and password
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin123"

    def __init__(self):
        self.has_admin_access = False

    def admin_access(self, request):
        '''
        Read the username and password from the request
        validate the username and password for admin access.
        Flag that the user has admin access.
        '''

        # Getting Username & Password from the request
        username = request.get('username')
        password = request.get('password')

        # validate username and password
        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            self.has_admin_access = True # Admin Access granted as valid credentials.
        else:
            self.has_admin_access = False # No admin access as invalid credentials

        return self.has_admin_access


# Simulate a request
request = {'username': 'admin', 'password': 'admin123'}
user = User()
print(user.admin_access(request))  # The output should be True because the passed request has correct admin credentials.