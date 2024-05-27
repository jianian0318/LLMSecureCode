import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    clean_content = re.sub('<script.*?>.*?</script>', '', content, flags=re.MULTILINE|re.DOTALL) 
    return clean_content