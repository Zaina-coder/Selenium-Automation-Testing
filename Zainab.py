import datetime
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(100)
driver.get('https://en.wikipedia.org/')
assert "Wikipedia, the free encyclopedia" in driver.title
driver.find_element(By.ID, 'searchInput').send_keys('Python (programming language)')
driver.find_element(By.ID, 'searchButton').click()
assert "Python (programming language)" in driver.title
print('Title is correct')


time.sleep(5)
driver.quit()
driver.close()


