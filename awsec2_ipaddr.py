#!/usr/bin/python3.6
import pycurl
from io import BytesIO

# Determine Public IP address of EC2 instance
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'checkip.amazonaws.com')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
# Body is a byte string, encoded. Decode it first.
print (body.decode('iso-8859-1').strip())
