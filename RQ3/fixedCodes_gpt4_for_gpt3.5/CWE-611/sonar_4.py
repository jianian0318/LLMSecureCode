import xml.sax

def get_root():
    parser = xml.sax.make_parser()
    # Disable DTD Processing to fix CWE-611 vulnerability
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setFeature(xml.sax.handler.feature_external_pes, False)
    
    handler = xml.sax.ContentHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler.root