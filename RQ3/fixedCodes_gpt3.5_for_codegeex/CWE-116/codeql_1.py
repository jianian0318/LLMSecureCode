import re

def filterScriptTags(content):
    return re.sub(r'<script.*?>.*?</script>', '', content, flags=re.IGNORECASE)

print(filterScriptTags('<script>alert("Hello, world!")</script>'))