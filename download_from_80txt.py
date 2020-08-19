# -*- coding = utf-8 -*-
# @Time : 2020/8/16 14:43
# @Author :
# @File : download_from_80txt.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup
import re


def download_from_80txt(book_name):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }

    url = 'http://www.txt80.com/e/search/index.php'

    # post时 通过抓包获取传递的参数
    params = {
        'tbname': 'download',
        'tempid': '1',
        'keyboard': book_name,
        'Submit22': '搜索',
        'show': 'title,softsay,softwriter'
    }

    # post方式获取html文件
    html = requests.post(url, params)

    # print(html.text)
    link = ''

    # 设定匹配模式
    findTitle = re.compile(r'<a .*>《(.*?)》全本TXT电子书下载</a>')
    findLink = re.compile(r'<a href="(.*?)" target="_blank">')
    soup = BeautifulSoup(html.text, "html.parser")
    for item in soup.find_all('div', class_='slist'):

        # BeautifulSoup获取的item必须转换成字符串 才能使用正则表达式
        item = str(item)
        # 通过正则表达式获得数据
        title = re.findall(findTitle, item)[0]
        if title == book_name:
            link = re.findall(findLink, item)[0]
            break

    if len(link) == 0:
        print("无此书籍")
        return False

    link = 'http://www.txt80.com' + link

    html = requests.get(link, headers=headers)
    html.encoding = html.apparent_encoding

    soup = BeautifulSoup(html.text, "html.parser")
    item = soup.find_all('div', class_='downlinks')
    item = str(item)
    findLink = re.compile(r'<a href="(.*?)" target="_blank">进入小说下载地址</a>')
    link = re.findall(findLink, item)[0]

    link = 'http://www.txt80.com' + link
    html = requests.get(link, headers=headers)
    html.encoding = html.apparent_encoding

    soup = BeautifulSoup(html.text, "html.parser")
    item = soup.find_all('div', class_='downlist')
    item = str(item)
    findLink = re.compile(r'<a href="(.*?)".*下载到电脑（右键另存）')
    link = re.findall(findLink, item)[0]

    print("开始下载")
    down_res = requests.get(link, headers=headers)
    with open(book_name+'.txt', "wb") as code:
        code.write(down_res.content)

    print("finish")
    return True


