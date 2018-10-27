#
# movie.py
# @author Wuriqilang
# @description 
# @created Sat Oct 27 2018 11:02:43 GMT+0800 (中国标准时间)
# @last-modified Sat Oct 27 2018 23:42:10 GMT+0800 (中国标准时间)
#

# 3.7
import requests
from bs4 import BeautifulSoup


def getOnePaget(n):  # 获取一个网页
    url = f'http://maoyan.com/board/4?offset={n * 10}'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    # 调用
    r = requests.get(url, headers=header)

    return r.text


def Parse(text,count):
    # 初始化
    soup = BeautifulSoup(text,"lxml")
    soup.prettify()
    names= soup.find_all(attrs={'class':'name'})
    stars= soup.find_all(attrs={'class':'star'})
    releastimes= soup.find_all(attrs={'class':'releasetime'})

    for i in range(len(names)):
        print("第",count*10+1+i,"名"+names[i].string)
        print(stars[i].string.strip())
        print(releastimes[i].string)
        print("================================================================")


for i in range(10):
    data = getOnePaget(i)
    Parse(data,i)


