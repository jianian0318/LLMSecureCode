from bs4 import BeautifulSoup

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all <script> tags in the HTML 
    script_tags = soup.find_all('script')
    
    # Remove the <script> tags 
    for tag in script_tags:
        tag.decompose()
    
    # Output the cleaned HTML as a string
    return str(soup)