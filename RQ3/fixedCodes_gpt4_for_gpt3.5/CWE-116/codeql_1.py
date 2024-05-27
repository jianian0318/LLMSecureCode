import html

def filterScriptTags(content):
    '''
    Remove and escape <script> tags from the content argument to prevent Cross-Site Scripting attacks.
    '''
    content = html.escape(content)
    return content