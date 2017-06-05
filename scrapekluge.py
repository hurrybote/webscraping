# -*- coding:utf-8 -*-

import os
import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'http://klug-fx.jp/fxnews/archives.php?month=200901'
# DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver')

# SEARCH_WORD = '政治'

def getText(date, month_url):
    browser.get(month_url)
    time.sleep(3)

    links = browser.find_elements_by_xpath('//ul[@class="phase1_article_list"]/li/a')
    for link in links:
        html = urlopen(link.get_attribute("href"))
        bsObj = BeautifulSoup(html.read(), "html.parser")
        # text = bsObj.find("h1").string
        text = bsObj.find("p", {"class":"phase1_texts"}) 
        print(text.string)
        time.sleep(2)


if __name__ == '__main__':
    month_url = []
    date_url = []
    try:
        browser = webdriver.PhantomJS()
        browser.get(URL)
        time.sleep(3)
        
        links = browser.find_elements_by_xpath('//tbody/tr/td/a')
        for link in links:
            max_date = int(link.text)
            # print(max_date)
            month_url.append(link.get_attribute("href"))
            
        
        for date in range(0, max_date-1):
            # print(date)
            # print(type(date))
            getText(date, month_url[date])

    finally:
        browser.quit()

