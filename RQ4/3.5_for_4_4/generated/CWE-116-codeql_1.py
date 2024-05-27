import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Construct the pattern for <script> tags
    script_pattern = re.compile(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', re.IGNORECASE)

    # Replace <script> tags with an empty string
    cleaned_content = re.sub(script_pattern, '', content)
    
    return cleaned_content