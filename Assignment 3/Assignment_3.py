# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Biolage homepage
driver.get("https://www.biolage.com/")
# Maximize the window
driver.maximize_window()
time.sleep(3)

# Click on hair care option
hair_care = driver.find_element("xpath","/html/body/div[1]/header/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/nav/ul/li[3]/div[2]/a")
hair_care.click()
time.sleep(3)

# Click on shop option of product
shop_now = driver.find_element("xpath","/html/body/div[1]/main/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/a")
shop_now.click()
time.sleep(3)

# Click on buy now option
buy_now = driver.find_element("xpath","/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[4]/div[1]/button")
buy_now.click()
time.sleep(3)

# Click on styling
styling = driver.find_element("xpath","/html/body/div[1]/header/div/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/nav/ul/li[4]/div[2]/a")
styling.click()
time.sleep(3)

#Click on shop now
shop = driver.find_element("xpath","/html/body/div[1]/main/div/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div[1]/a")
shop.click()
time.sleep(3)

# Click on buy now option
buy = driver.find_element("xpath","/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[4]/div[1]/button")
buy.click()
time.sleep(3)

# Click on add to list option
add = driver.find_element("xpath","/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]")
add.click()
time.sleep(3)

driver.close()
