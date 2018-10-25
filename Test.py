# coding=utf-8


# 用来抓取网页的html源码
import requests
# 取随机数
import random
# 时间相关操作
import time

# 用于代替正则式 取源码中相应标签中的内容
from bs4 import BeautifulSoup


def get_content(url, data=None):
    # 设置Headers
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'br, gzip, deflate',
        'Accept-Language': 'zh-cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))

    while True:
        try:
            req = requests.get(url=url, headers=header, timeout=timeout)
            break
        except Exception as e:
            print('3'+e)
            time.sleep(random.choice(range(8, 15)))
        return req.text


if __name__ == '__main__':
    url = 'http://www.biqukan.com/0_790/21725523.html'
    html = get_content(url)
    print(html)
