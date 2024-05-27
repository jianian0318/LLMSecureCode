from defusedxml import defusedxml

def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    try:
        # Extract xpath and xml from the GET request
        xpath_val = request.GET.get('xpath')
        xml_val = request.GET.get('xml')
        
        # Parse the XML string
        python_object = defusedxml.defuse_stdlib(xml_val)
        
        # Create XPath query
        query = "/tag[@id='{}']".format(xpath_val)
        
        # Apply XPath query and get result
        result = python_object.xpath(query)
        
        # Return the result
        return HttpResponse(result)

    except Exception as e:
        # Return a generic error message
        return HttpResponse('An error occurred while processing your request.')