import os
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    '''
    Retrieve the "password" from the GET request,
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    PASSWORD_EXPECTED = os.getenv("PASSWORD_EXPECTED")  # Retrieve password from environment variables
    password_received = request.GET.get("password", "")

    if password_received == PASSWORD_EXPECTED:
        return redirect('/login/')  # Assumes the login page is at /login/
    else:
        return HttpResponse("Unauthorized", status=401)