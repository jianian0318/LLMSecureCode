import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use Regex to remove content within and inclusive of <script> </script> tags
    clean_content = re.compile(r'<.*?>')
    return re.sub(clean_content, '', content)