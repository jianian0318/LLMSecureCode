# Importing necessary libraries
from lxml import etree
from io import StringIO
from django.http import HttpResponse

# Function to process XPath queries on XML Data
def xpath_query(request):
    try:
        # Get the `xpath` value from the GET request
        xpath = request.GET.get('xpath')

        # Get the 'xml' value from the GET request
        xml_str = request.GET.get('xml')

        # Constructing and parsing the xml payload
        parser = etree.XMLParser(ns_clean=True)
        tree   = etree.parse(StringIO(xml_str), parser)

        # Building xpath query
        query = f"/tag[@id={xpath}]"

        # Querying the XML with XPath and getting result
        element = tree.xpath(query)
        result = etree.tostring(element[0])

        return HttpResponse(result)

    except Exception as e:
        # Return the exception message in case of an error
        return HttpResponse(str(e))