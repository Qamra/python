import requests
newsurl = 'http://news.sina.com.cn/o/2017-11-15/doc-ifynvxeh4994555.shtml'
res = requests.get(newsurl)
res.encoding = 'utf-8' #python预测编码未ISO，手动定为utf-8
print(res.text)

from bs4 import BeautifulSoup
html_sample = '\
<html> \
<body> \
<h1 id="title">Hello World</h1> \
<a href="#" class="link">This is link1</a> \
<a href="# link2" class="link">This is link2</a> \
</body> \
</html>'

#取出含有特定标签的html元素
soup = BeautifulSoup(html_sample,'html.parser') #将非结构化数据转为结构化
header = soup.select('h1') #取出包含h1标签的元素，hearder类型为list
print(header[0].text) #取出文字

alink = soup.select('a') #找出含有a标签的元素
for link in alink: #输出元素的内容
    print(link['href'])
"""
#取出含有特定CSS属性的元素
title = soup.select('#title') #取id里面的内容，必须要在具体内容前面加上‘#’
print(title)

for link in soup.select('.link'): #取class里面的内容，加上.
    print(link)
print(soup.select('.link'))"""

a = '<a href="#" qo=123 tu=456>i am a link</a>'
soup2 = BeautifulSoup(a,'html.parser')
print(soup2.select('a')[0]['qo'])
