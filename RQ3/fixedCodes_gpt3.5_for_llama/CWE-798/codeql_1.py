from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    '''
    Retrieve the "password" from the GET request.
    Compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password')
    if password == 'secret':
        return redirect('login')
    else:
        return HttpResponse('Invalid password')