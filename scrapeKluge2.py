# -*- coding:utf-8 -*-

import os
import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

# URL = 'http://klug-fx.jp/fxnews/detail.php?id=26906'
# browser = webdriver.PhantomJS()
# browser.get(URL)

#ブラウザー
# def webDriver():
#     browser.get(URL)
#     time.sleep(2)
#テキストを書き込む関数
def getText(bsObj):
    # html = urlopen(browser.current_url)
    # bsObj = BeautifulSoup(html.read(), "html.parser")
    text = bsObj.find("p", {"class":"phase1_texts"})
    time.sleep(2)
    print(text)

#次の記事に進む関数
def getNextURL(bsObj):
    next_url = bsObj.find("ul", {"class":"phase1_pagenav"}).find_all("a")
    for url in next_url:
        link = url.get("href")
    # link = 'http://klug-fx.jp'+ URL
    # print(link)
    return link
    time.sleep(2)

if __name__ == '__main__':
    try:
        URL = 'http://klug-fx.jp/fxnews/detail.php?id=26906'
        browser = webdriver.PhantomJS()
        browser.get(URL)
        while(browser.find_elements_by_xpath('//ul[@class="phase1_pagenav"]/li[2]/a')!=None):
            html = urlopen(browser.current_url)
            bsObj = BeautifulSoup(html.read(), "html.parser")
            getText(bsObj)
            URL = 'http://klug-fx.jp' + getNextURL(bsObj)
            browser.get(URL)
            # webDriver(browser, URL)
        # print(browser.current_url)

        # html = urlopen(browser.current_url)
        # bsObj = BeautifulSoup(html.read(), "html.parser")
        # text = bsObj.find("p", {"class":"phase1_texts"})
        # next_url = bsObj.find("ul", {"class":"phase1_pagenav"}).find_all("a")
        # time.sleep(2)
        # for url in next_url:
        #     URL = url.get("href")
        # URL = 'http://klug-fx.jp'+ URL
        # time.sleep(2)

        # print(link)
        # print(text)

    finally:
        browser.quit()