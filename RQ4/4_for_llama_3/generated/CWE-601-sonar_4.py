    from django.http import HttpResponseRedirect, HttpResponse


    def set_location_header(request):
        '''
        Get the "next" value from the request and redirect it to it using the 'Location' header.
        '''
        next_url = request.GET.get('next', '')
        if next_url:
            response = HttpResponseRedirect(next_url)
            response['Location'] = next_url
            return response
        else:
            return HttpResponse('No "next" value found in the request.')
    