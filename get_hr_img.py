import urllib.request
import re
url = 'https://www.hackerrank.com/certificates/9716A794874D'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    if match:
        print('Image URL:', match.group(1))
    else:
        print('No og:image found')
except Exception as e:
    print('Error:', e)
