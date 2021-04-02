#!/bin/usr/python

import requests
import hashlib
import re

req = requests.session()
url = "http://139.59.178.146:32460"

### Get Request
rget = req.get(url)
html = rget.content # saving the get request

### strip HTML
def html_tags(html):
    clean = re.compile('<.*?>')
    clean_content = re.sub(clean, '',str(html))
    raw_content = clean_content.split('string')[1]
    return raw_content[0:20]
main_string = html_tags(html)
### md5 encrypt
md5_hash = hashlib.md5(main_string.encode()).hexdigest()
print(md5_hash)
### POST Request
data = dict(hash=md5_hash)
rpost = req.post(url,data=data)

print(rpost.text)
