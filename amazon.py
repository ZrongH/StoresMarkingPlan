#!/usr/bin/python
# coding:utf-8
import os


__author__ = 'ZrongH'

import urllib2
import time
from bs4 import BeautifulSoup
import selenium.webdriver

__author__ = 'ZrongH'
driver = selenium.webdriver.PhantomJS(
    executable_path=r'I:\phantomjs-1.9.1-windows\phantomjs-1.9.1-windows\phantomjs')


def return_folder():
    folder_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    if not os.path.isdir(folder_name):
        os.makedirs(folder_name)
    return folder_name


def return_class_folder(class_name):
    class_folder_parent = return_folder()
    class_folder = os.path.join(class_folder_parent, class_name)
    if not os.path.isdir(class_folder):
        os.makedirs(class_folder)
    return class_folder


def download(url, from_where, class_name):
    folder_name = return_class_folder(class_name)
    f = urllib2.urlopen(url)
    data = f.read()
    name = folder_name + '/' + from_where + str(time.time()) + '.jpg'
    with open(name, "wb") as code:
        code.write(data)


def download_book(img_url, from_where):
    download(img_url, from_where, 'book')


def download_earphone(img_url, from_where):
    download(img_url, from_where, 'earphone')


def amazon_book_plan():
    driver.get('http://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051')
    web_elements = driver.find_elements_by_class_name('bannerImage')
    for element in web_elements:
        text = driver.execute_script("return arguments[0].innerHTML;", element)
        soup = BeautifulSoup(text)
        img_url = soup.find(['img']).get('src')
        print img_url
        download_book(img_url, 'amazon')


def amazon_earphone_plan():
    driver.get('http://www.amazon.cn/MP3-MP4-%E9%9F%B3%E7%AE%B1-%E8%80%B3%E6%9C%BA/b/ref=topnav_storetab_mp?ie=UTF8&node=760233051')
    web_elements = driver.find_elements_by_class_name('bannerImage')
    for element in web_elements:
        text = driver.execute_script("return arguments[0].innerHTML;", element)
        soup = BeautifulSoup(text)
        img_url = soup.find(['img']).get('src')
        print img_url
        download_earphone(img_url, 'amazon')


def jd_book_plan():
    driver.get('http://book.jd.com/')
    web_element = driver.find_element_by_class_name('slide-items')
    text = driver.execute_script("return arguments[0].innerHTML;", web_element)
    soup = BeautifulSoup(text)
    for li in soup.find_all('li'):
        imgUrl = li.find(['img']).get('src')
        print imgUrl
        download_book(imgUrl, 'jd')

def jd_earphone_plan():
    driver.get('http://channel.jd.com/652-828.html')
    web_element = driver.find_element_by_id('slide')
    text = driver.execute_script("return arguments[0].innerHTML;", web_element)
    soup = BeautifulSoup(text)
    for li in soup.find_all('li'):
        imgUrl = li.find(['img']).get('src')
        print imgUrl
        download_earphone(imgUrl, 'jd')

def dangdang_book_plan():
    driver.get('http://book.dangdang.com/')
    web_element = driver.find_element_by_id('slidecontent')
    text = driver.execute_script("return arguments[0].innerHTML;", web_element)
    soup = BeautifulSoup(text)
    for li in soup.find_all('li'):
        img_url = li.find(['img']).get('original')
        print img_url
        download_book(img_url, 'dangdang')


def close_driver():
    driver.quit()


def book_plan():
    amazon_book_plan()
    jd_book_plan()
    dangdang_book_plan()


def earphone_plan():
    jd_earphone_plan()
    amazon_book_plan()

if __name__ == '__main__':
    book_plan()
    earphone_plan()
    #time.sleep(1)
    #jd_book_plan()
    #time.sleep(1)
    #dangdang_book_plan()
    close_driver()
    #print return_class_folder('book')
