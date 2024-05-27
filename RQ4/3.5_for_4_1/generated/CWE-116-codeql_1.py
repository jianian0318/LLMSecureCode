import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # This regular expression will match any script tags with any content inside them
    script_tag_re = re.compile(r'<script\b[^>]*>(.*?)</script>', re.DOTALL | re.IGNORECASE)

    # This line will substitute any matched script tags with an empty string effectively removing them
    cleaned_content = re.sub(script_tag_re, '', content)
    
    return cleaned_content