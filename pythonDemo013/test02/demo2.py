#-*- coding: UTF-8 -*- ��
'''
Created on 2016.9.7
@author: xieb
'''
import urllib2
import cookielib
from bs4 import BeautifulSoup

url = "http://www.runoob.com/"

print "第三种方法"
cj =cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 =urllib2.urlopen(url)
#print response3.getcode()
#print cj
#print response3.read()
#print len(response3.read())


content = ''

soup = BeautifulSoup(response3.read(),'html.parser',from_encoding='UTF-8')

links = soup.find_all('a')
for link in links:
    print link.name,link['href'],link.get_text()