from defusedxml.sax import parse

class ConfigHandler:
    def __init__(self):
        self.root = None

    def startElement(self, name, attrs):
        if self.root is None:
            self.root = name

def get_root():
    handler = ConfigHandler()
    parse('resources/config.xml', handler)
    return handler.root

if __name__ == '__main__':
    root = get_root()
    print(root)