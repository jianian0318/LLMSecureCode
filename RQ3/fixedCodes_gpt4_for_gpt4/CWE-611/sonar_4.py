import xml.sax

class MyHandler(xml.sax.ContentHandler):
    pass

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setFeature(xml.sax.handler.feature_external_pes, False)
    parser.setContentHandler(MyHandler())
    parser.parse('resources/config.xml')

get_root()