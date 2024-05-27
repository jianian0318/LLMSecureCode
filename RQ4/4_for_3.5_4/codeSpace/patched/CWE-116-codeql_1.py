import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use regular expression to remove <script> tags
    filtered_content = re.sub(r'<script.*?>.*?</script>', '', content)

    return filtered_content