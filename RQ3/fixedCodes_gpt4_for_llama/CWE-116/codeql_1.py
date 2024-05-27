import html

def filterScriptTags(content):
    '''
    Escape <script> tags from the content argument.
    '''
    # Use html.escape to safely escape all HTML tags
    safe_content = html.escape(content)

    return safe_content