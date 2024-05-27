# Define usernames and passwords that have admin access
ADMIN_CREDENTIALS = {"username1": "password1", "username2": "password2"}

# Define a mock request class for understanding
class Request:
    def __init__(self, username: str, password: str):
        self.username=username
        self.password=password
  

HAS_ADMIN_ACCESS = False

def admin_access(request):
    '''
    Read the username and password from the request.
    Validate the username and password for admin access.
    Flag that the user has admin access.
    '''
    global HAS_ADMIN_ACCESS
      
    # Read the username and password from the request
    username = request.username
    password = request.password

    # Validate the username and password for admin access
    for admin_username, admin_password in ADMIN_CREDENTIALS.items():
        if username == admin_username and password == admin_password:
            # Flag that the user has admin access
            HAS_ADMIN_ACCESS = True
            break
    else:
        HAS_ADMIN_ACCESS = False
       
    return HAS_ADMIN_ACCESS


# Testing it with admin username and password
request = Request("username1", "password1")
print(admin_access(request))  # Should return True 

# Testing it with non-admin username and password
request = Request("not-admin", "password")
print(admin_access(request))  # Should return False