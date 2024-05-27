    from django.http import HttpResponseRedirect, HttpResponse


    def set_location_header(request):
        next_url = request.GET.get('next', '/')
        response = HttpResponse()
        response['Location'] = next_url
        return response
    