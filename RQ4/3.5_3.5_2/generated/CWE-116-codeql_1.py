def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use regex pattern to find <script> tags
    pattern = r'<script.*?>.*?</script>'
    
    # Use re.sub() function to remove <script> tags
    filtered_content = re.sub(pattern, '', content)
    
    return filtered_content