#
# fanyi.py
# @author Wuriqilang
# @description 
# @created Sat Oct 13 2018 09:27:09 GMT+0800 (中国标准时间)
# @last-modified Sat Oct 27 2018 19:51:58 GMT+0800 (中国标准时间)
#



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
