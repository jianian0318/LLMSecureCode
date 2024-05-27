from defusedxml.lxml import parse
from django.http import HttpResponse
from io import StringIO

def xpath_query(request):
    '''
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload using defusedxml to mitigate XML attacks,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml,
    avoid leaking internal exception details.
    '''
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    if not xpath or not xml:
        return HttpResponse("Missing required parameters", status=400)

    try:
        xml_payload = StringIO(xml)
        xml_tree = parse(xml_payload)  # Using defusedxml to parse XML data
        result = xml_tree.xpath(xpath)
        return HttpResponse(str(result))
    except Exception:
        # Respond with a generic error message instead of leaking exception details
        return HttpResponse("An error occurred while processing the XML data.", status=400)

# Make sure to define other required parts of your Django application,
# like urlpatterns and WSGI configuration if you plan to run this code.