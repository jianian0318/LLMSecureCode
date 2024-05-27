from django.http import HttpResponseRedirect


def set_location_header(request):
    # Get the "next" value from the request
    next_url = request.GET.get('next')

    if next_url:
        # Redirect to the "next" value using the 'Location' header
        response = HttpResponseRedirect(next_url)
        response['Location'] = next_url
        
        return response
    else:
        return HttpResponse("No 'next' value provided in the request")