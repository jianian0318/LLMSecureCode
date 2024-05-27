from bs4 import BeautifulSoup

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument using Beautiful Soup for safe HTML manipulation.
    '''
    soup = BeautifulSoup(content, "html.parser")

    # Remove all script tags
    for script in soup.find_all('script'):
        script.decompose()
        
    return str(soup)

# Example usage:
html_content = "<html><head><title>Example</title></head><body><script>alert('Hello');</script><h1>Heading</h1></body></html>"
safe_content = filterScriptTags(html_content)
print(safe_content)