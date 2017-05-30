from selenium import webdriver


driver = webdriver.PhantomJS()
driver.get("https://t21.nikkei.co.jp/g3/CMNDF11.do")
print(driver.find_element_by_id("content").text)