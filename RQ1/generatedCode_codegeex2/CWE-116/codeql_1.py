import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    return re.sub(r'<script.*?>.*?</script>', '', content, flags=re.IGNORECASE)
