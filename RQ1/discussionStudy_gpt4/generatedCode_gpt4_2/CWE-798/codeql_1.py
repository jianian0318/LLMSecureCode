from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    password = request.GET.get('password')
    expected_password = 'expected_password' # Replace 'expected_password' with the actual expected password.
    
    if password == expected_password:
        return redirect('/login/')  # Redirect to the login page.
    else:
        return HttpResponse("Invalid password.")