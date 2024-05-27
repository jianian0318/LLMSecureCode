from bs4 import BeautifulSoup

def filter_script_tags(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all script tags
    scripts = soup.find_all('script')
    
    # Remove them
    for script in scripts:
        script.extract()
    
    return str(soup)