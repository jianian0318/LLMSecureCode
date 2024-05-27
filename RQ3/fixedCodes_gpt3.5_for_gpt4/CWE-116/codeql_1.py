import re
import html

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    script_pattern = re.compile('<script.*?>.*?</script>', re.IGNORECASE)
    cleaned_content = re.sub(script_pattern, '', content)
    cleaned_content = html.escape(cleaned_content)
    
    return cleaned_content