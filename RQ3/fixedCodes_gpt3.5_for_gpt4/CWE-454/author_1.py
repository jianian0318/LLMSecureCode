ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def admin_access(request):
    username = request.get('username')
    password = request.get('password')

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        has_admin_access = True
    else:
        has_admin_access = False
        
    return has_admin_access

request = {'username': 'admin', 'password': 'admin123'}
print(admin_access(request))