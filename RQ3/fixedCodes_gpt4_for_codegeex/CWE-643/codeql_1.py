from lxml import etree
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    '''
    xpath = request.GET.get('xpath', '')
    xml = request.GET.get('xml', '')

    # Construct and parse the xml payload
    xml_payload = f'<root>{xml}</root>'
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(xml_payload), parser)
    
    # Perform the XPath query
    xpath_expr = etree.XPath(f'/tag[@id=$path]')
    result = xpath_expr(tree, path=xpath)

    # Return the result
    return HttpResponse(result)