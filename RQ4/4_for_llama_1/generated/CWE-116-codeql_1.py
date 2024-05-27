from bs4 import BeautifulSoup

def filterScriptTags(content):
    soup = BeautifulSoup(content, "html.parser")

    # Find and extract all <script> tags
    for script in soup("script"):
        script.extract()

    return str(soup)

# Example usage:
content = "<p>This is a paragraph.</p><script>alert('Hello!');</script><p>This is another paragraph.</p>"
filtered_content = filterScriptTags(content)
print(filtered_content)