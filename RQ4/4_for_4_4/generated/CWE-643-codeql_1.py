from defusedxml.lxml import parse as defused.parse
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the XML payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
     '''
    # Get the `xpath` value from the GET request
    xpath = request.GET.get('xpath')

    # Get the 'xml' value from the GET request
    xml = request.GET.get('xml')

    # Check if xpath and xml are specified
    if not xpath or not xml:
        return HttpResponse(status=400)

    # Construct and parse the XML payload
    tree = defusedxml.parse(StringIO(xml))

    # Construct the XPath search string
    search_string = f"/tag[@id='{xpath}']"

    # Perform the XPath query
    result = tree.xpath(search_string)

    if result:
        return HttpResponse(result[0], content_type = "text/xml")
    else:
        return HttpResponse(status=404)