from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select



s = Service("./chromedriver.exe")
chrome_browser = webdriver.Chrome(service=s)

chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/input-form-demo.html")

user_message = chrome_browser.find_element_by_name('first_name')
user_message2 = chrome_browser.find_element_by_name('last_name')
user_message3 = chrome_browser.find_element_by_name('email')
user_message4 = chrome_browser.find_element_by_name('phone')
user_message5 = chrome_browser.find_element_by_name('address')
user_message6 = chrome_browser.find_element_by_name('city')
drop = Select(chrome_browser.find_element_by_name('state'))  
user_message7 = chrome_browser.find_element_by_name('zip')
user_message8 = chrome_browser.find_element_by_name('website')
user_message9 = chrome_browser.find_element_by_name('comment')


user_message.send_keys("John")
user_message2.send_keys("Smith")
user_message3.send_keys("smith@g.com")
user_message4.send_keys("(555) 555-1234")
user_message5.send_keys("White House")
user_message6.send_keys("London")  
drop.select_by_index(3)
user_message7.send_keys("72716")
user_message8.send_keys("www.facebook.com")
chrome_browser.find_element_by_css_selector("input[type='radio']").click()
user_message9.send_keys("lorem ipsum")
chrome_browser.find_element_by_xpath(".//button[contains(@class,'btn btn-default') and @type='submit']").click()


# chrome_browser.quit()