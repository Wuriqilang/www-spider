#coding=utf-8

import requests
from urllib import request

if __name__=='__main__':
    response=request.urlopen("https://www.baidu.com")
    html=response.read()
    print(html)

