import os
import time
from selenium import webdriver

URL = 'https://news.yahoo.co.jp/'
# DRIVER_PATH = os.path.join(os.path.dirname(__file__), 'chromedriver')

SEARCH_WORD = '政治'

if __name__ == '__main__':
    try:
        browser = webdriver.PhantomJS()
        browser.get(URL)
        print (browser.page_source)
        time.sleep(3)
        search_input = browser.find_element_by_name('p')
        print (search_input)
        search_input.send_keys(SEARCH_WORD)
        search_input.submit()
        time.sleep(3)
        print(browser.title)
        titles = browser.find_elements_by_xpath('//h2[@class="t"]')
        for title in titles:
            link = title. find_element_by_tag_name('a')
            print(link.get_attribute("href"))
            
    finally:
        browser.quit()


