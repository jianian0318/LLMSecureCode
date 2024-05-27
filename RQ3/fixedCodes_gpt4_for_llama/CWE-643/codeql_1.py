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
    xpath = request.GET.get('xpath')
    xml = request.GET.get('xml')

    if not xpath or not xml:
        return HttpResponse("Missing required parameters", status=400)

    try:
        xml_tree = etree.parse(StringIO(xml))

        parser = etree.XMLParser(resolve_entities=False)
        safe_xpath = etree.XPath(xpath, parser=parser)

        result = safe_xpath(xml_tree)
        
        return HttpResponse(str(result), status=200)
    except Exception as e:
        return HttpResponse(str(e), status=500)