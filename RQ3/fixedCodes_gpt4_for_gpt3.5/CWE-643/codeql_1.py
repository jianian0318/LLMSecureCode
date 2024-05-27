from lxml import etree
from io import StringIO
from django.http import HttpResponse
from defusedxml.lxml import fromstring
from defusedxml.common import EntitiesForbidden

def xpath_query(request):
    try:
        xpath = request.GET.get('xpath')
        xml = request.GET.get('xml')

        parser = etree.XMLParser(resolve_entities=False)
        xml_tree = fromstring(xml, parser=parser)
        result = xml_tree.find(".//tag[@id='{}']".format(xpath))
        return HttpResponse(result)
    except EntitiesForbidden:
        return HttpResponse('Invalid XML: entity reference forbidden', status=400)
    except etree.XMLSyntaxError:
        return HttpResponse('Invalid XML', status=400)