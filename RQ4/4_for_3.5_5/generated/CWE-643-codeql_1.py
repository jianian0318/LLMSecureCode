def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''

    xpath = request.GET.get('xpath', '')  # Get the `xpath` value from the GET request
    xml = request.GET.get('xml', '')  # Get the 'xml' value from the GET request

    parser = etree.XMLParser()
    tree = etree.parse(StringIO(xml), parser)  # Construct and parse the xml payload

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    result = tree.xpath(xpath.format('value'))
    return HttpResponse(result)