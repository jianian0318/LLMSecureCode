import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # use regular expressions (re.sub) to replace <script> tags (and their contents) with an empty string
    clean_content = re.sub(r'<script\b[^>]*>.*?</script>', '', content, flags=re.DOTALL)

    return clean_content