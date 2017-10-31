

import pickle

class Bird(object):
    have_feather = True
    reproduction_method = "egg"
    write = "ok"



with open("summer.txt","rb") as f:
    summer = pickle.load(f)
print(summer.have_feather)


#time

import datetime,time
"""
start = time.clock()
for i in range(100000):
    print(i**2)

end = time.clock()
print(end - start)"""
st = time.gmtime()
st = time.localtime()
s = time.mktime(st)
print(st)

t = datetime.date(2017,10,12)
print(t)

import re
m = re.search("[0-9]","abcd4ef")
print(m.group())
n = re.search(pattern="12",string="0151235")
print(n.group())
a = re.match(pattern="234",string="12345")
print(a)

str = re.sub(pattern="12",repl="45",string="01263")
print(str)

import http.client
conn = http.client.HTTPConnection("www.example.com")
conn.request("GET","/")
response = conn.getresponse()

print(response.status,response.reason)
content = response.read()
print(content)



