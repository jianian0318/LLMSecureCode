from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings

def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password')
    if password == settings.SECRET_PASSWORD:
        return redirect('/login/')
    else:
        return HttpResponse('Invalid password')