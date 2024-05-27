from defusedxml import lxml as etree
from io import StringIO

from django.http import HttpResponse


def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    # Get the `xpath` value
    xpath_val = request.GET.get('xpath')
    # Get the `xml` value
    xml_val = request.GET.get('xml')
    
    # Parse the XML string and construct an ElementTree
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False)
    tree = etree.parse(StringIO(xml_val), parser)
    
    # Build the XPath query
    query = f"/tag[@id='{xpath_val}']"
    
    # Execute the XPath query
    result = tree.xpath(query)
    
    # Convert the result to String
    result_str = etree.tostring(result[0], pretty_print=True)
    
    # Return the result as HTTP response
    return HttpResponse(result_str)