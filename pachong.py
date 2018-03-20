import http.client

conn = http.client.HTTPConnection("www.cnblogs.com")
conn.request("GET","/vamei")
response = conn.getresponse()

content = response.read()
print(content)

import re

pattern = "posted @ (\d{4}-[0,1]\d-{0,3}\d [0,2]\d:[0-6]\d)Vamei  \((\d+)\) "
for line in content:
    m = re.search(pattern,line)
    if m != None:
        print(m.group(1),m.group(2))

