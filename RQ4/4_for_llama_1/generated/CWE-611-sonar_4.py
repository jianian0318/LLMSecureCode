from defusedxml import defusedxml

class ConfigHandler(defusedxml.sax.ContentHandler):
    def __init__(self):
        self.root = None
        self.current = None

    def startElement(self, name, attrs):
        if self.root is None:
            self.root = {
                'name': name,
                'attributes': attrs,
                'children': []
            }
            self.current = self.root
        else:
            child = {
                'name': name,
                'attributes': attrs,
                'children': []
            }
            self.current['children'].append(child)
            self.current = child

    def endElement(self, name):
        self.current = self.current['parent']

    def get_root(self):
        return self.root

def parse_config():
    parser = defusedxml.sax.make_parser()
    handler = ConfigHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler.get_root()

if __name__ == '__main__':
    root = parse_config()
    print(root)