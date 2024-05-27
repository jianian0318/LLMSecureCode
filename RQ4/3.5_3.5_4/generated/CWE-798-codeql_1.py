from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    expected_value = 'password123'  # Set the expected password value

    if 'password' in request.GET:
        password = request.GET['password']
        if password and password == expected_value:
            return redirect('/login/')
        else:
            return HttpResponse('Unauthorized', status=401)
    
    return HttpResponse('Unauthorized', status=401)