#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests

resp=requests.get('https://www.baidu.com') #请求百度首页
#print resp #打印请求结果的状态码
print resp.content #打印请求到的网页源码
