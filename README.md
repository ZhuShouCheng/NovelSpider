PythonSpider
基本流程


获得html文件
html = requests.post(url, params)
设定匹配模式
findXXX = re.compile(r'')
创建bs对象
soup = BeautifulSoup(html.text, "html.parser")
将大概位置使用bs分割出来
for item in soup.find_all('div', class_=''):
使用正则表达式精准匹配
title = re.findall(findXXX, item)[0]



