import defusedxml.sax as dxsax

class XMLHandler(dxsax.ContentHandler):
    def __init__(self):
        self.root = None
        self.current = None
        self.tag_stack = []

    def startElement(self, name, attrs):
        self.tag_stack.append(name)
        if self.root is None:
            self.root = {
                'tag': name,
                'attrs': attrs,
                'children': []
            }
            self.current = self.root
        else:
            new_item = {
                'tag': name,
                'attrs': attrs,
                'children': []
            }
            self.current['children'].append(new_item)
            self.current = new_item

    def endElement(self, name):
        self.tag_stack.pop()
        if len(self.tag_stack) > 0:
            self.current = self.root
            for tag in self.tag_stack:
                for child in self.current['children']:
                    if child['tag'] == tag:
                        self.current = child
                        break

    def get_root(self):
        return self.root

def get_root():
    handler = XMLHandler()
    dxsax.parse('resources/config.xml', handler)
    return handler.get_root()