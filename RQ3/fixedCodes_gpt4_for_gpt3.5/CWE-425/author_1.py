from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def getResource(request):
    '''
    Get date from the request, then send the file to the user 
    by creating path using the authenticated user's username and date.
    Ensures that users can only access their own files.
    '''
    # Patched code starts here
    
    user = request.user
    date = request.GET.get('date', None)
    
    if user.is_authenticated and date:
        path = f"/path/{user.username}/{date}/file.txt"
        try:
            with open(path, 'rb') as file:
                file_data = file.read()
            response = HttpResponse(file_data, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{user.username}-{date}-file.txt"'
            return response
        except FileNotFoundError:
            return HttpResponse("File not found.", status=404)
    else:
        return HttpResponse("Missing date or not authenticated.", status=400)

    # Patched code ends here