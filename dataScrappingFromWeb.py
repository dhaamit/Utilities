import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# 1. Bypass SSL certificate verification (common cause for similar errors)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

try:
    # 2. Add a User-Agent header to pretend you are a browser
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # 3. Pass the request AND the SSL context to urlopen
    html = urllib.request.urlopen(req, context=ctx).read()
    
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

except Exception as e:
    print(f"Failed to retrieve {url}")
    print(f"Error: {e}")
