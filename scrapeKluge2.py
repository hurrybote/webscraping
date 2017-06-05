# -*- coding:utf-8 -*-

import os
import time
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

#テキストを書き込む関数
def getText(bsObj, text_data):
    # html = urlopen(browser.current_url)
    # bsObj = BeautifulSoup(html.read(), "html.parser")
    text = bsObj.find("p", {"class":"phase1_texts"})
    date = bsObj.find("dl", {"class":"phase1_publish_time"}).find_all("dd")[0]
    head = bsObj.h1
    data_list = [head,date,text]
    time.sleep(2)
    writeCSV(text_data, data_list)
    print(text)
    print(date)
    print(head)

#次の記事に進む関数
def getNextURL(bsObj):
    next_url = bsObj.find("ul", {"class":"phase1_pagenav"}).find_all("a")
    for url in next_url:
        link = url.get("href")
    # link = 'http://klug-fx.jp'+ URL
    # print(link)
    return link
    time.sleep(2)

def writeCSV(text_data, data_list):
    if os.path.exists("./kluge_fx.csv"):
        with open('./kluge_fx.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(data_list)
    else:
        with open('./kluge_fx.csv', 'w') as f:
            text_data.append(data_list)
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(text_data)
            writer.writerow(data_list)

if __name__ == '__main__':
    text_data = ['head','date','text','景気', '物価','金利','マネーサプライ','貿易収支'
    ,'雇用','個人消費','介入','要人発言','他通貨','石油', '政治', '株', '債権']
    data_list = []
    try:
        URL = 'http://klug-fx.jp/fxnews/detail.php?id=26906'
        browser = webdriver.PhantomJS()
        browser.get(URL)
        while(browser.find_elements_by_xpath('//ul[@class="phase1_pagenav"]/li[2]/a')!=None):
            html = urlopen(browser.current_url)
            bsObj = BeautifulSoup(html.read(), "html.parser")
            getText(bsObj, text_data)
            URL = 'http://klug-fx.jp' + getNextURL(bsObj)
            browser.get(URL)


    finally:
        browser.quit()