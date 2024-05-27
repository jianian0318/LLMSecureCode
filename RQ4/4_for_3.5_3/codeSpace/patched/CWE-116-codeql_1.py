import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use regular expressions to find and replace <script> tags with an empty string
    content = re.sub('<script.*?>.*?</script>', '', content)

    return content