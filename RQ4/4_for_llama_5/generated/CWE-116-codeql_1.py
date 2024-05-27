from bs4 import BeautifulSoup

def filter_script_tags(content):
  '''
  Remove <script> tags from the content argument.
  '''
  # Parse the content using BeautifulSoup
  soup = BeautifulSoup(content, features="lxml")

  # Find all <script> tags in the parsed content
  for script in soup(["script"]):
    # Remove the script tags
    script.decompose()

  # Get the content back in plain text, without <script> tags
  filtered_content = soup.get_text()

  return filtered_content