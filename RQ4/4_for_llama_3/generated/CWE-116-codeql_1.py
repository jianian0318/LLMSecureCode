from bs4 import BeautifulSoup

def filterScriptTags(content):
    soup = BeautifulSoup(content, "html.parser")
    
    # Find all script tags
    for script in soup("script"):
        # Remove them
        script.decompose()
        
    return str(soup)

# Example usage
content = "<html><body><script>alert('hello')</script></body></html>"
filtered_content = filterScriptTags(content)
print(filtered_content)