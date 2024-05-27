from bs4 import BeautifulSoup

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument using BeautifulSoup library.
    '''
    soup = BeautifulSoup(content, 'html.parser')

    # Find all <script> tags in the html
    script_tags = soup.find_all('script')
    
    # Remove identified script tags
    for tag in script_tags:
        tag.decompose()  # remove tag and its contents

    # Return the sanitized html as a string
    return str(soup)