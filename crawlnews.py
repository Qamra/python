import requests
from bs4 import BeautifulSoup
"""
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text,'html.parser')

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time,h2,a)
"""
res = requests.get('http://news.sina.com.cn/c/2017-11-19/doc-ifynwnty5237992.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')

contents = soup.select('#artibodyTitle')[0].text
time = soup.select('.time-source')[0].contents[0].strip()

from datetime import datetime
dt = datetime.strptime(time,'%Y年%m月%d日%H:%M')

mediasource = soup.select('.time-source span a')[0].text
print(dt,mediasource,contents)

article = []
for p in soup.select('#artibody p')[:-1]:
    article.append(p.text.strip())
    ''.join(article)
print(article)
#print('''简短格式''')
#article1 = ''.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
#print(article1)

editor = soup.select('.article-editor')[0].text.strip('责任编辑：')
print(editor)

commentcount = soup.select('#commentCount1')
print(commentcount)

