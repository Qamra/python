import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

#获取某个新闻信息
def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text
    result['newssource'] = soup.select('.time-source span a')[0].text
    timesource = soup.select('.time-source')[0].contents[0].strip()
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
    result['comments'] = getCommentCounts(newsurl)
    print(result)

commentURL = "http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1512380009721_68805192"

#获取新闻评论数
def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml', newsurl) #正则表达式取新闻ID
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid)) #format方法
    jd = json.loads(comments.text.strip('var loader_1512380009721_68805192='))
    return jd['result']['count']['total']

news = 'http://news.sina.com.cn/gov/2017-12-04/doc-ifypikwt6211765.shtml'

print(getCommentCounts(news))
print(getNewsDetail(news))



