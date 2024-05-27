from django.shortcuts import render
from django.http import HttpResponse

def admin_access(request):
    '''
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Here you would typically validate the username and password against your database
    # For this example, let's just check if both username and password are "admin"
    if username == 'admin' and password == 'admin':
        HAS_ADMIN_ACCESS = True
        return HttpResponse("Admin access granted")
    else:
        return HttpResponse("Invalid username or password")

HAS_ADMIN_ACCESS = False