from html.parser import HTMLParser

class ScriptRemover(HTMLParser):
    """
    Subclass of HTMLParser that removes <script> tags from HTML content.
    """
    def __init__(self):
        super().__init__()
        self.filtered_content = ""
        self.within_script_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.within_script_tag = True

    def handle_endtag(self, tag):
        if tag == 'script':
            self.within_script_tag = False

    def handle_data(self, data):
        if not self.within_script_tag:
            self.filtered_content += data

    def handle_entityref(self, name):
        if not self.within_script_tag:
            self.filtered_content += f'&{name};'

    def handle_charref(self, name):
        if not self.within_script_tag:
            self.filtered_content += f'&#{name};'

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument by using HTMLParser.
    '''
    parser = ScriptRemover()
    parser.feed(content)
    return parser.filtered_content

# Example usage
example_html = "<p>Hello, <script type='text/javascript'>alert('Not good');</script>world!</p>"
print(filterScriptTags(example_html))