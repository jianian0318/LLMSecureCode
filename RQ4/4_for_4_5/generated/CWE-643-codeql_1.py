from io import StringIO
from django.http import HttpResponse
from defusedxml import lxml
from django.utils.http import urlencode

def xpath_query(request):
    # Get the `xpath` value from the GET request
    xpath = request.GET.get('xpath', default='')

    # Get the 'xml' value from the GET request
    xml_string = request.GET.get('xml', default='')
    
    # Construct and parse the XML payload
    try:
        xml_tree = lxml.parse(StringIO(xml_string))
    except lxml.etree.XMLSyntaxError as e:
        return HttpResponse(f"Invalid XML: {e}", status=400)

    # Return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    query = f"/tag[@id='{xpath}']"  # Assuming 'xpath' variable contains the ID value
    try:
        result = xml_tree.xpath(query)
    except lxml.etree.XPathEvalError as e:
        return HttpResponse(f"Invalid XPath: {e}", status=400)

    # Convert results to string for HttpResponse
    result_str = ''.join([lxml.etree.tostring(e, encoding='unicode') for e in result])

    return HttpResponse(result_str, content_type="text/xml")