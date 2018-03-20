import requests
doc = requests.get('http://news.sina.com.cn/china/')
#print(doc.encoding)
doc.encoding = 'utf-8'
#print(doc.text)

from bs4 import BeautifulSoup
txt = BeautifulSoup(doc.text,'html.parser')
print(txt.select('.news-item'))