from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
@login_required
def getResource(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        if request.user.username == username:
            file_path = f'/path/to/files/{username}/{date}/file.txt'
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
            else:
                return render(request, 'error.html', {'error': 'File not found'})
        else:
            raise Http404("You do not have access to this file")
    else:
        return render(request, 'error.html', {'error': 'Invalid request'})