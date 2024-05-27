import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):

    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    # retrieve the password from the environment variable
    secret_password = os.getenv('SECRET_PASSWORD')
   
    password = request.GET.get('password')
    if password == secret_password:
        return redirect('/login/')
    else:
        return HttpResponse('Invalid password')