#coding=utf-8
import chardet
from urllib import request
import ssl


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context #全局声明 ssl证书
    response = request.urlopen("http://fanyi.baidu.com/")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)

