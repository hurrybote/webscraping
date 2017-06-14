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
    # if(bsObj.find("dl", {"class":"phase1_publish_time"}).find_all("dd")[0].get_text() != None):
    text = bsObj.find("p", {"class":"phase1_texts"}).get_text()
    date = bsObj.find("dl", {"class":"phase1_publish_time"}).find_all("dd")[0].get_text()
    head = bsObj.h1.get_text()
    data_list = [head,date,text]
    # time.sleep(5)
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


def writeCSV(text_data, data_list):
    if os.path.exists("./kluge_fx_2016.csv"):
        with open('./kluge_fx_2016.csv', 'a') as f:
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(data_list)
    else:
        with open('./kluge_fx_2016.csv', 'w') as f:
            # text_data.append(data_list)
            writer = csv.writer(f, lineterminator='\n')
            list = [text_data, data_list]
            writer.writerows(list)

            # writer.writerow(text_data)
            # writer.writerow(data_list)


def BS(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    return bsObj
    # time.sleep(3)
    # getText(bsObj, text_data)
    # URL = klug_url + getNextURL(bsObj)
    # # time.sleep(5)
    # browser.get(URL)


if __name__ == '__main__':
    text_data = ['head','date','text','イベント','景気', '物価','金利','マネーサプライ','貿易収支'
    ,'雇用','個人消費','介入','要人発言','他通貨','石油', '政治', '株', '債権']
    data_list = []
    try:
        URL = 'http://jp.reuters.com/resources/archive/jp/20090101.html'
        browser = webdriver.PhantomJS()
        browser.get(URL)
        # time.sleep(3)
        while(browser.find_elements_by_xpath('//a[@class="pageNext"]')!=None):
            html = urlopen(browser.current_url)
            bsObj_top = BeautifulSoup(html.read(), "html.parser")
            urls = bsObj_top.find("div", {"class":"module"}).find_all("div",{"class":"headlineMed"}).find_all("a")
            urls.reverse()
            for url in urls:
                link = klug_url+url.get("href")
                data = BS(link)
                getText(data, text_data)
            # getNextURL(bsObj_top)
            browser.get(klug_url + getNextURL(bsObj_top))

    finally:
        browser.quit()