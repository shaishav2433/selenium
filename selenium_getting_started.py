from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = 'E:\Selenium\chromedriver.exe'
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--incognito") # OPTIONAL
# option.add_argument("--headless") # OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.get("https://www.google.com")

search = browser.find_element_by_name('q')
search.send_keys ("BITCOIN")
time.sleep(5)
#search.send_keys (" BITCOIN")
#search.send_keys (keys.ENTER)
domain_name.submit()

#print(driver.title)

#driver.quit()