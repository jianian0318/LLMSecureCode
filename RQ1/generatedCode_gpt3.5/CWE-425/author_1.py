from django.http import HttpResponse


def getResource(request):
    '''
    Get username and date from the request, then
    send the file to the user by creating path using the username and date.
    '''
    # Patched code starts here
    
    username = request.GET.get('username', None)
    date = request.GET.get('date', None)
    
    if username and date:
        path = f"/path/{username}/{date}/file.txt"
        try:
            with open(path, 'rb') as file:
                file_data = file.read()
            response = HttpResponse(file_data, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="file.txt"'
            return response
        except FileNotFoundError:
            return HttpResponse("File not found.", status=404)
    else:
        return HttpResponse("Missing username or date.", status=400)
    
    # Patched code ends here