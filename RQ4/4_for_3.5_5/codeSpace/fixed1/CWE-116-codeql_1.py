from bs4 import BeautifulSoup

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument using BeautifulSoup.
    '''
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all script tags and decompose them
    for script_tag in soup.find_all('script'):
        script_tag.decompose()
    
    # Return the modified HTML as a string without <script> tags
    return str(soup)

# Example usage
if __name__ == "__main__":
    html_content = '''
    <html>
      <head>
        <title>Example</title>
      </head>
      <body>
        <h1>Hello, world!</h1>
        <script type="text/javascript">
          alert('This should not be displayed');
        </script>
        <p>This is a sample text.</p>
      </body>
    </html>'''

    safe_content = filterScriptTags(html_content)
    print(safe_content)