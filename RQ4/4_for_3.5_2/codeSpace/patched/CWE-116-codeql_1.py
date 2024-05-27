import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''

    # Create a regex pattern to match <script> tags
    pattern = re.compile(r'<script.*?</script>', re.DOTALL)
    
    # Use the sub() function from the re module to replace all occurrences of the pattern with an empty string
    filtered_content = re.sub(pattern, '', content)
    
    return filtered_content