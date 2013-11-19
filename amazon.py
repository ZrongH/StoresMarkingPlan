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


def returnFolder():
    folderName = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    if not os.path.isdir(folderName):
        os.makedirs(folderName)
    return folderName


def download(url, fromWhere):
    FolderName = returnFolder()
    f = urllib2.urlopen(url)
    data = f.read()
    name = FolderName + '/' + fromWhere + str(time.time()) + '.jpg'
    with open(name, "wb") as code:
        code.write(data)


def amazonBookPlan():
    driver.get('http://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sa_menu_top_books_l1?ie=UTF8&node=658390051')
    webElements = driver.find_elements_by_class_name('bannerImage')
    for element in webElements:
        text = driver.execute_script("return arguments[0].innerHTML;", element)
        soup = BeautifulSoup(text)
        imgUrl = soup.find(['img']).get('src')
        print imgUrl
        download(imgUrl, 'amazon')



def jdBookPlan():
    driver.get('http://book.jd.com/')
    webElement = driver.find_element_by_class_name('slide-items')
    text = driver.execute_script("return arguments[0].innerHTML;", webElement)
    soup = BeautifulSoup(text)
    for li in soup.find_all('li'):
        imgUrl = li.find(['img']).get('src')
        print imgUrl
        download(imgUrl, 'jd')


def dangdangBookPlan():
    driver.get('http://book.dangdang.com/')
    webElement = driver.find_element_by_id('slidecontent')
    text = driver.execute_script("return arguments[0].innerHTML;", webElement)
    soup = BeautifulSoup(text)
    for li in soup.find_all('li'):
        imgUrl = li.find(['img']).get('original')
        print imgUrl
        download(imgUrl, 'dangdang')

def closeDriver():
    driver.quit()


if __name__ == '__main__':
    amazonBookPlan()
    # time.sleep(1)
    jdBookPlan()
    # time.sleep(1)
    dangdangBookPlan()
    closeDriver()
