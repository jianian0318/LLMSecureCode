import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Pattern to match opening <script> tags, any content within, and closing </script> tags
    script_pattern = re.compile(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', re.DOTALL | re.IGNORECASE)

    # Substitute all matches with an empty string
    clean_content = re.sub(script_pattern, '', content)

    return clean_content