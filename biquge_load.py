# -*- coding = utf-8 -*-
# @Time : 2020/8/16 18:52
# @Author :
# @File : biquge_load.py
# @Software: PyCharm


# 项目说明： 由于该网站使用了js加载文字 导致requests无法获得到完整html源代码
# 因此 使用了selenium自动化工具辅助完成  因而限制了程序的运行速度以及要求
# 未来真正投入使用只能架设在服务器上


# https://www.sbiquge.com/s.php?ie=gbk&q=
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re

def getData(url,book_name):
    link = 'https://www.sbiquge.com' + url
    html = requests.get(link, headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    item = str(soup.find_all('div', class_='showtxt')[0])

    text = re.findall(r'<div id="content" class="showtxt">(.*?)</div>', item)
    print(text)

    return



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
book_name = '剑仙在此'
url = 'https://www.sbiquge.com/s.php?ie=gbk&q=' + book_name

html = requests.get(url, headers)
findLink = re.compile(r'<a href="(.*?)">')
soup = BeautifulSoup(html.text, 'html.parser')
item = str(soup.find_all('div', class_='p10')[0])

link = re.findall(findLink, item)[0]
link = 'https://www.sbiquge.com' + link
print(link)
html = requests.get(link, headers)
findLink = re.compile(r'<a href="(.*?)">')
soup = BeautifulSoup(html.text, 'html.parser')
for item in soup.find_all('dd'):
    item = str(item)
    link = re.findall(findLink, item)[0]

    link = 'https://www.sbiquge.com' + link

    # 使用selenium工具获得完整html文件
    browser = webdriver.Chrome()
    browser.get(link)
    html = browser.page_source

    # html = requests.get(link, headers)
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_='showtxt')
    # print(html.text)
    item = str(item)
    # print(item)
    findText = re.compile(r'<div.*?class="showtxt".*?>(.*?)</div>', re.S)
    text = re.findall(findText, item)[0]
    text.replace('<br/>', '')
    print(text)
    browser.close()

    break
    #  数据储存部分未实现






