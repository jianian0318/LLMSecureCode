import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    cleaned_content = re.sub('<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    return cleaned_content