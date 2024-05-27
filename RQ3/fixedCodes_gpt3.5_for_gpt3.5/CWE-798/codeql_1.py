from django.http import HttpResponse
from django.shortcuts import redirect


def process_request(request):
    password = request.GET.get('password')
    expected_password = 'admin1234'

    if password and password == expected_password:
        return redirect('/login')

    return HttpResponse('Invalid password')