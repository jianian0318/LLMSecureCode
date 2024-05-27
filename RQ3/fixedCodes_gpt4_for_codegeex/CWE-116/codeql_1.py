import html

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    content = html.escape(content)
    return content