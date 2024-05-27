from defusedxml.lxml import parse
from io import StringIO

from django.http import HttpResponse

def xpath_query(request):
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    if not xpath or not xml:
        return HttpResponse("Missing required parameters", status=400)

    try:
        xml_tree = parse(StringIO(xml))
        result = xml_tree.xpath(xpath)
    except Exception as e:
        # The message returned to the client should be generic
        # And should not give away information about the server-side error or stack trace
        return HttpResponse("Error processing request", status=400)

    return HttpResponse(str(result))