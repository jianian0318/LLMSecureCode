from django.http import HttpResponse
from django.shortcuts import redirect
import os


def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password_from_request = request.GET.get('password')

    expected_password = os.getenv('EXPECTED_PASSWORD')   # retrieve 'EXPECTED_PASSWORD' from environment variable

    if password_from_request == expected_password:
        return redirect('login')

    return HttpResponse('Password is incorrect')