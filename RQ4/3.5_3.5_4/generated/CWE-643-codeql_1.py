def xpath_query(request):
    xpath = request.GET.get('xpath')  # Get the 'xpath' value from the GET request
    xml = request.GET.get('xml')  # Get the 'xml' value from the GET request

    parser = etree.XMLParser()
    root = etree.parse(StringIO(xml), parser)  # Construct and parse the xml payload

    result = root.xpath(f"/tag[@id='{xpath}']")  # Perform the XPath query "/tag[@id={}]" format from the parsed xml

    return HttpResponse(result)  # Return the result of the XPath query as HttpResponse