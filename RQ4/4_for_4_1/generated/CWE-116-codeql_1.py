import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # use regex to replace script tags with an empty string
    content = re.sub("<script[^>]*>.*?</script>", "", content, flags=re.DOTALL)
    
    return content