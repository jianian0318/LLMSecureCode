from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def process_request(request):
    '''
    Retrieve the "password" from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    password = request.GET.get('password', None)
    expected_password = get_expected_password()  # Function to fetch expected password from a secure location
    if password == expected_password:
        return redirect('/login')  # Modify with actual login URL
    else:
        messages.error(request, 'Invalid password!')
        return HttpResponse('Invalid password!')