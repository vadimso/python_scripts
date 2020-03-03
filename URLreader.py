#!/usr/bin/env python3.6
import urllib.request
import sys

print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

URL="http://www.asos.com"
#print(URL)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"

try:
    ## Read page
    print(URL)
    req = urllib.request.Request(URL, headers=headers)
    resp = urllib.request.urlopen(req)
    pageContent = resp.read()
    pageContent = pageContent.decode('utf-8')
    Answer = '200'
    print('Answer:200')

except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    Answer = e.code
    print('HTTPError: {}'.format(e.code))

except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    Answer = e.reason
    print('URLError: {}'.format(e.reason))
finally:
    print(Answer)
