# -*- coding: UTF-8 -*-
from urllib import request
import ssl

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context #全局声明 ssl证书
    req = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(req)
    print("geturl打印信息：%s"%(response.geturl()))
    print('**********************************************')
    print("info打印信息：%s"%(response.info()))
    print('**********************************************')
    print("getcode打印信息：%s"%(response.getcode()))
