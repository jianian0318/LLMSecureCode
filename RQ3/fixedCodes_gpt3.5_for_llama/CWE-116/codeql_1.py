import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use a regular expression to find all <script> tags
    script_tags = re.findall(r'<script.*?/script>', content, re.DOTALL)

    # Replace each script tag with an empty string
    for script_tag in script_tags:
        content = content.replace(script_tag, '')

    # Encode the content to prevent any script injection
    content = content.encode('html')

    return content