# import urllib.request
# response = urllib.request.urlopen('https://python.org')
# print(response.read().decode('utf-8'))

# import urllib.request
# response = urllib.request.urlopen('https://python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# import urllib.request
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'word': 'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())


# import urllib.request
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
#     print(response.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time out')


# import urllib.request
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# # print(response.read().decode('utf-8'))
# print(response.getheaders())



# from urllib import  request, parse
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict),encoding='utf-8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# print(browser.current_url)


# """
# import requests
# from bs4 import BeautifulSoup
# import pymysql
# import time
# import lxml
#
# def get_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text,'lxml')
#     return soup
# def get_links(link_url):
#     soup = get_page(link_url)
#     links_div = soup.find_all('div',class_='lazyloaded')
#     links = [div.a.get('href') for div in links_div]
#     return links
# def get_house_info(house_url):
#     soup = get_page(house_url)
#     price = soup.find('span',class_='content__list--item-price').text
#     unit = soup.find('span',class_='unit').text.strip()
#     area = 'test'
#     info = {
#         '价格':price,
#         '单位':unit,
#         '面积':area
#     }
#     return info
# DataBase = {
#         'host':'127.0.0.1',
#         'database':'exam',
#         'user':'root',
#         'password':'123456',
#         'charset':'utf8mb4',
#         'port':'3306'
#
#     }
# def get_db(setting):
#     return pymysql.connect(**setting)
# def insert(db,house):
#     values = "'{}',"*2 +"'{}'"
#     sql_values = values.format(house['价格'],house['单位'],house['面积'])
#     sql = """
#     # insert house(price,unit,area) values({})
#     """.format(sql_values)
#     cursor = db.cursor
#     cursor.execute(sql)
#     db.commit()
# db = get_db(DataBase)
# links = get_links('https://bj.lianjia.com/zufang/')
# for link in links:
#     time.sleep(2)
#     house = get_house_info(link)
#     insert(db,house)
# """


