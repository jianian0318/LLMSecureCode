from django.http import HttpResponse
import os

def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    '''
    username = request.GET.get('username')
    date = request.GET.get('date')

    if username and date:
        file_path = os.path.join(username, date)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                return HttpResponse(f.read(), content_type='application/octet-stream')
        else:
            return HttpResponse("File not found", status=404)
    else:
        return HttpResponse("Username or date not provided", status=400)
