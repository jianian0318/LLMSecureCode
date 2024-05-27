import xml.sax
from xml.sax.handler import ContentHandler

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, name):
        child = Node(name)
        child.parent = self
        self.children.append(child)
        return child

class ConfigHandler(ContentHandler):
    def __init__(self):
        self.root = None
        self.current = None
        self.text = ""

    def startElement(self, name, attrs):
        if self.current is not None:
            self.current = self.current.add_child(name)
        else:
            self.root = Node(name)
            self.current = self.root

    def endElement(self, name):
        if self.current.parent is not None:
            self.current = self.current.parent

    def characters(self, content):
        self.text += content

def get_root():
    parser = xml.sax.make_parser()
    handler = ConfigHandler()
    parser.setContentHandler(handler)
    parser.parse("resources/config.xml")
    return handler.root