from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recording = 0 
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag != 'script':
            self.data.append(f'<{tag}>')

    def handle_endtag(self, tag):
        if tag != 'script':
            self.data.append(f'</{tag}>')

    def handle_data(self, data):
        self.data.append(data)

def filterScriptTags(content):
    parser = MyHTMLParser()
    parser.feed(content)
    filtered_content = ''.join(parser.data)
    return filtered_content