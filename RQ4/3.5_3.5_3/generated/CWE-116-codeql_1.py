import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Use BeautifulSoup to parse and remove <script> tags
    from bs4 import BeautifulSoup
    
    # Create a BeautifulSoup object with the content
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all <script> tags in the soup and remove them
    scripts = soup.find_all('script')
    for script in scripts:
        script.extract()
    
    # Get the filtered content from the soup
    filtered_content = str(soup)
    
    return filtered_content