from defusedxml.lxml import parse
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    # Get the 'xpath' value from the GET request
    xpath = request.GET.get('xpath')

    # Get the 'xml' value from the GET request
    xml = request.GET.get('xml')

    # Construct the XML payload and parse it
    root = parse(StringIO(xml))

    # Construct the XPath query
    query = "/tag[@id={}]".format(xpath)

    # Execute the XPath query on the parsed XML
    result = root.xpath(query)

    # Return the result of the XPath query
    return HttpResponse(result)