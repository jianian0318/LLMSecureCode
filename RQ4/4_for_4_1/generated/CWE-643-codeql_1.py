def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath = request.GET.get('xpath')
    
    # Get the 'xml' value from the GET request
    xml = request.GET.get('xml')

    # Construct and parse the xml payload
    parser = etree.XMLParser(remove_blank_text=True)
    xml_payload = StringIO(xml)
    tree = etree.parse(xml_payload, parser)
    
    # Format the xpath query
    xpath_query = "/tag[@id='{}']".format(xpath)
    
    # Execute the_xpath_query
    result = tree.xpath(xpath_query)

    # Return the result of the XPath query
    return HttpResponse(result)