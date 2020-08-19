# -*- coding = utf-8 -*-
# @Time : 2020/8/16 14:13
# @Author :
# @File : NovelSpider.py
# @Software: PyCharm

import re
from bs4 import BeautifulSoup
import urllib.request, urllib.error
from download_from_80txt import download_from_80txt

URLlist = []

def main():
    bookname = ''
    download_from_80txt(bookname)






if __name__ == '__main__':
    main()