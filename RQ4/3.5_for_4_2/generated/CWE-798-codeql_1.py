from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    '''
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    '''
    
    # Replace the hardcoded password with a secure method of retrieving credentials
    expected_password = get_expected_password()
    
    # Retrieve the 'password' from the GET request
    password = request.GET.get("password")
    
    # Comparing the password with the expected value.
    if password == expected_password:
        # If it is the same, redirect to the login page.
        return redirect('login')
    else:
        # If it's not, return a simple HttpResponse stating it's incorrect.
        return HttpResponse("Incorrect password.")