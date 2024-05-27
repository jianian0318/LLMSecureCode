from bs4 import BeautifulSoup

def filter_script_tags(content):
    soup = BeautifulSoup(content, 'html.parser')

    # Search and destroy <script> tags from soup.
    for script in soup("script"):
        script.decompose()

    # Return the sanitized text
    return str(soup)

# Example usage:
content = '<p>This is a paragraph.</p><script>alert("Hello!");</script>'
filtered_content = filter_script_tags(content)
print(filtered_content)  # Output: <p>This is a paragraph.</p>