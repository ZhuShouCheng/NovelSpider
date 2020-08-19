# -*- coding = utf-8 -*-
# @Time : 2020/8/18 13:41
# @Author :
# @File : BaiduWenKu.py
# @Software: PyCharm

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


# 借鉴别人的项目  在有关driver.execute_script上不上很了解
# 项目本身因此存在一个广告 难以正常运行


# r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print(driver.page_source)

# options = webdriver.ChromeOptions()
# options.add_argument(
#     'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('https://wk.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')




# options = webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
# driver = webdriver.Chrome(chrome_options = options)
# driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
# url = driver.current_url
# if 'bfetype=new' in url:
#     elem = driver.find_element_by_class_name('btn-close')
#
#
# page = driver.find_elements_by_xpath("//div[@class='page']")
# driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去
# nextpage = driver.find_element_by_xpath("//a[@data-fun='next']")
# nextpage.click()