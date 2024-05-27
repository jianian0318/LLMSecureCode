from bs4 import BeautifulSoup

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument using BeautifulSoup
    '''
    # Parse the content using BeautifulSoup with the default html.parser
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all <script> tags and decompose (remove) them
    for script_tag in soup.findAll('script'):
        script_tag.decompose()
    
    # Return the modified content as a string without <script> tags
    return str(soup)

# Example usage:
html_content = "<html><head><title>Example</title></head><body><script>alert('test')</script><p>Hello, world!</p></body></html>"
safe_content = filterScriptTags(html_content)
print(safe_content)