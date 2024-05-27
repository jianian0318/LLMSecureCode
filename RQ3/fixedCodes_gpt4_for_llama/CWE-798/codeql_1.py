# Your code is indeed vulnerable because you are using a hard-coded password ('secret'). A more secure approach would be to set the password as an environment variable so it isn't hard-coded into your application. Here is your fixed code:

import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password')
    if password == os.getenv('SECRET_PASSWORD'):
        return redirect('login')
    else:
        return HttpResponse('Invalid password')

# Remember, you need to set the environment variable `SECRET_PASSWORD` in your system or in your hosting service. It will be safer and easier to change anytime.